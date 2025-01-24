from aws_cdk import App, Stack
from constructs import Construct
from my_cdk.vpc import VpcNetwork
from my_cdk.ec2_instance import Ec2Instance

class Ec2VpcStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create VPC
        vpc_network = VpcNetwork(self, "MyVpcNetwork")
        vpc = vpc_network.get_vpc()

        # Create EC2 instance within the VPC
        ec2_instance = Ec2Instance(self, "MyEc2Instance", vpc=vpc)

app = App()
Ec2VpcStack(app, "Ec2VpcStack")

app.synth()
