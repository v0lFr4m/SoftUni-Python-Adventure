from project.clients.base_client import BaseClient

class BusinessClient(BaseClient):
    def update_discount(self):
        if self.total_orders >= 2:
            self.discount : float = 10
        else:
            self.discount : float = 0