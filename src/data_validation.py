import pandas as pd
import numpy as np
from datetime import datetime
import json
from pathlib import Path

class FlightDataValidator:
    def __init__(self, data_path):
        self.data_path = data_path
        self.report_path = 'data/reports/validation_report.json'
        self.results = {
            'errors': [],
            'warnings': [],
            'passed_tests': 0,
            'failed_tests': 0
        }
        
    def load_data(self):
        """Carrega os dados do arquivo CSV"""
        try:
            self.df = pd.read_csv(
                self.data_path,
                parse_dates=['departure_time', 'scheduled_arrival', 'actual_arrival']
            )
            return True
        except Exception as e:
            self._add_error(f"Falha ao carregar dados: {str(e)}")
            return False
    
    def _add_error(self, message):
        self.results['errors'].append(message)
        self.results['failed_tests'] += 1
        
    def _add_warning(self, message):
        self.results['warnings'].append(message)
        
    def _add_success(self, message):
        self.results['passed_tests'] += 1
    
    def validate_schema(self):
        """Valida o schema básico dos dados"""
        required_columns = {
            'flight_id': 'object',
            'airline': 'object',
            'origin': 'object',
            'destination': 'object',
            'status': 'object',
            'flight_duration': 'int64',
            'delay_minutes': 'float64'
        }
        
        for col, dtype in required_columns.items():
            if col not in self.df.columns:
                self._add_error(f"Coluna obrigatória faltando: {col}")
            elif str(self.df[col].dtype) != dtype:
                self._add_warning(f"Tipo incorreto para {col}. Esperado: {dtype}, Encontrado: {self.df[col].dtype}")
            else:
                self._add_success(f"Validação de schema para {col}")
    
    def validate_values(self):
        """Validações específicas de valores"""
        
        if (self.df['flight_duration'] < 0).any():
            self._add_error("Duração de voo negativa encontrada")
        
        
        valid_status = ['on_time', 'delayed', 'canceled', 'diverted', 'overbooked']
        invalid_status = ~self.df['status'].isin(valid_status)
        if invalid_status.any():
            self._add_error(f"Status inválidos encontrados: {self.df[invalid_status]['status'].unique()}")
            
        
        if self.df['flight_id'].duplicated().any():
            self._add_error("IDs de voo duplicados encontrados")
    
    def validate_temporal_logic(self):
        """Valida a lógica temporal"""
        
        canceled_with_arrival = self.df[(self.df['status'] == 'canceled') & 
                                       (self.df['actual_arrival'].notna())]
        if len(canceled_with_arrival) > 0:
            self._add_error(f"Voos cancelados com horário de chegada: {len(canceled_with_arrival)}")
    
    def generate_report(self):
        """Gera relatório de validação"""
        Path(self.report_path).parent.mkdir(exist_ok=True)
        with open(self.report_path, 'w') as f:
            json.dump(self.results, f, indent=2)
    
    def run_all_tests(self):
        """Executa todas as validações"""
        if self.load_data():
            self.validate_schema()
            self.validate_values()
            self.validate_temporal_logic()
            self.generate_report()
        
        return self.results