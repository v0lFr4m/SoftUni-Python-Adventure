from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.leaf_plant import LeafPlant
from project.plants.flower import Flower


class FlowerShopManager:
    VALID_PLANTS_TYPE = ['Flower', 'LeafPlant']
    VALID_CLIENT_TYPE = ['RegularClient', 'BusinessClient']
    def __init__(self):
        self.income : float = 0
        self.plants: list[BasePlant] = []
        self.clients : list[BaseClient] = []

    def add_plant(self, plant_type : str, plant_name : str , plant_price : float, plant_water_needed: int , plant_extra_data : str):
        if plant_type not in self.VALID_PLANTS_TYPE:
            raise ValueError("Unknown plant type!")

        if plant_type == 'Flower':
            plant = Flower(plant_name,plant_price,plant_water_needed,plant_extra_data)
            self.plants.append(plant)

        elif plant_type == 'LeafPlant':
            plant = LeafPlant(plant_name , plant_price , plant_water_needed , plant_extra_data)
            self.plants.append(plant)

        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type : str , client_name : str , client_phone_number : str):
        # check for valid client type
        if client_type not in self.VALID_CLIENT_TYPE:
            raise ValueError("Unknown client type!")

        # check for used phone number
        for client in self.clients:
            if client.phone_number == client_phone_number:
                raise ValueError("This phone number has been used!")

        if client_type == 'RegularClient':
            client = RegularClient(client_name, client_phone_number)
            self.clients.append(client)

        elif client_type == 'BusinessClient':
            client = BusinessClient(client_name , client_phone_number)
            self.clients.append(client)

        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):

        matching_clients = [c for c in self.clients if c.phone_number == client_phone_number]
        if not matching_clients:
            raise ValueError("Client not found!")
        client = matching_clients[0]

        matching_plants = [p for p in self.plants if p.name == plant_name]
        if not matching_plants:
            raise ValueError("Plants not found!")

        if len(matching_plants) < plant_quantity:
            return "Not enough plant quantity."

        sold_plants = []
        count = 0
        for plant in self.plants:
            if plant.name == plant_name:
                sold_plants.append(plant)
                count += 1
                if count == plant_quantity:
                    break

        for plant in sold_plants:
            self.plants.remove(plant)

        total_price = sum(plant.price for plant in sold_plants)
        order_amount = total_price * (1 - client.discount / 100)  # assuming discount is in percentage

        self.income += order_amount

        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self, plant_name : str):
        for plant in self.plants:
            if plant.name == plant_name:
                self.plants.remove(plant)
                return f"Removed {plant.plant_details()}"
        return "No such plant name."

    def remove_clients(self):
        client_count = len(self.clients)
        self.clients = [c for c in self.clients if c.total_orders > 0]
        remove_count = client_count - len(self.clients)
        return f"{remove_count} client/s removed."

    def shop_report(self):
        total_orders = sum(client.total_orders for client in self.clients)

        from collections import Counter

        plant_counter = Counter(plant.name for plant in self.plants)
        sorted_plants = sorted(plant_counter.items(), key=lambda x: (-x[1], x[0]))

        total_unsold_plants = sum(count for _, count in sorted_plants)


        sorted_clients = sorted(self.clients, key=lambda x: (-x.total_orders, x.phone_number))


        output_line = [
            "~Flower Shop Report~",
            f"Income: {self.income:.2f}",
            f"Count of orders: {total_orders}",
            f"~~Unsold plants: {total_unsold_plants}~~"
        ]

        for plant_name, count in sorted_plants:
            output_line.append(f"{plant_name}: {count}")

        output_line.append(f"~~Clients number: {len(sorted_clients)}~~")

        for client in sorted_clients:
            output_line.append(client.client_details())

        return "\n".join(output_line)
















