from aws_cdk import aws_ec2 as ec2, aws_iam as iam
from constructs import Construct

class Ec2Instance(Construct):
    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a security group for the EC2 instance
        security_group = ec2.SecurityGroup(self, "MySecurityGroup",
            vpc=vpc,
            allow_all_outbound=True,
            security_group_name="MySecurityGroup"
        )

        # Allow SSH access to the EC2 instance (port 22)
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(22),
            "Allow SSH access"
        )

        # Create an EC2 instance
        self.instance = ec2.Instance(self, "MyInstance",
            instance_type=ec2.InstanceType("t2.micro"),  # Choose your desired instance type
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            vpc=vpc,
            security_group=security_group
        )

       # Optionally, create an IAM role for the EC2 instance (if needed)
        role = iam.Role(self, "InstanceRole",
        assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            )   

        #Attach the IAM role to the EC2 instance
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEC2ReadOnlyAccess"))


    def get_instance(self):
        return self.instance
