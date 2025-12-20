from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    VALID_TYPES_ARTIFACTS = ["RenaissanceArtifact", "ContemporaryArtifact"]
    VALID_TYPE_COLLECTORS = ["Museum", "PrivateCollector"]
    def __init__(self):
        self.artifacts: list = []
        self.collectors: list = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self.VALID_TYPES_ARTIFACTS:
            raise ValueError("Unknown artifact type!")

        for artifact in self.artifacts:
            if artifact.name == artifact_name:
                raise ValueError(f"{artifact_name} has been already registered!")

        if artifact_type == "RenaissanceArtifact":
            new_artifact = RenaissanceArtifact(artifact_name, artifact_price, artifact_space)
            self.artifacts.append(new_artifact)
        elif artifact_type == "ContemporaryArtifact":
            new_artifact = ContemporaryArtifact(artifact_name , artifact_price , artifact_space)
            self.artifacts.append(new_artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."


    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.VALID_TYPE_COLLECTORS:
            raise ValueError("Unknown collector type!")

        for collector in self.collectors:
            if collector.name == collector_name:
                raise ValueError(f"{collector_name} has been already registered!")

        if collector_type == "Museum":
            new_collector = Museum(collector_name)
            self.collectors.append(new_collector)
        elif collector_type == "PrivateCollector":
            new_collector = PrivateCollector(collector_name)
            self.collectors.append(new_collector)

        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self,collector_name: str, artifact_name: str):
        collector = next((c for c in self.collectors if c.name == collector_name), None)
        if collector is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)
        if artifact is None:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."


        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required

        return f"{collector.name} purchased {artifact.name} for a price of {artifact.price:.2f}."

    def remove_artifact(self, artifact_name : str):
        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)
        if artifact is None:
            return "No such artifact."

        self.artifacts.remove(artifact)
        return 'Removed ' + artifact.artifact_information()

    def fundraising_campaigns(self,max_money: float):
        number_of_collectors = 0

        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                number_of_collectors += 1
        return f"{number_of_collectors} collector/s increased their available money."

    def get_auction_report(self):
        sold_artifacts = sum(len(c.purchased_artifacts) for c in self.collectors)
        available_artifacts = len(self.artifacts)

        output_line = [
            "**Auction statistics**",
            f"Total number of sold artifacts: {sold_artifacts}",
            f"Available artifacts for sale: {available_artifacts}",
            "***"
        ]
        # Sort collectors: by number of purchased artifacts desc, then by name asc
        sorted_collectors = sorted(self.collectors, key=lambda c: (-len(c.purchased_artifacts), c.name))

        for collector in sorted_collectors:
            output_line.append(str(collector))

        return "\n".join(output_line)

