from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class VpcNetwork(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a VPC
        self.vpc = ec2.Vpc(self, "MyVpc", max_azs=2)  # Maximum availability zones to use

    def get_vpc(self):
        return self.vpc
