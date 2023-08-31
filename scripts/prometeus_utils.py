import json,os

class PrometheusConnector:
    def __init__(self,nodes_file_name=None):
        self.prometheus_port = "9090"
        self.prom_api_path = "/api/v1/query_range"
        self.prom_point_api_path = "/api/v1/query"

        self.ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

        self.base_stack_config_path = f"{self.ROOT_PATH}/config"

        if nodes_file_name:
            self.nodes_file_path = f"{self.base_stack_config_path}/{nodes_file_name}"
            with open(self.nodes_file_path , 'r') as file:
                stack_details = json.load(file)
                
            self.monitoring_ip=  stack_details[stack_details["monitoring_node"]]["lan_ip"]
            self.prometheus_path = f"http://{self.monitoring_ip}:{self.prometheus_port}"

        self.GRAFANA_USERNAME="admin"
        self.GRAFANA_PASSWORD="admin123"
        self.GRAFANA_PORT = "3000"