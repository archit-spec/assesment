import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Bank as BankModel, Branch as BranchModel

class Bank(SQLAlchemyObjectType):
    class Meta:
        model = BankModel
        interfaces = (relay.Node, )

class Branch(SQLAlchemyObjectType):
    class Meta:
        model = BranchModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_banks = SQLAlchemyConnectionField(Bank)
    all_branches = SQLAlchemyConnectionField(Branch)
    branch = graphene.Field(Branch, ifsc=graphene.String(required=True))
    branches_by_bank = graphene.List(Branch, bank_name=graphene.String(required=True))

    def resolve_branch(self, info, ifsc):
        return BranchModel.query.filter_by(ifsc=ifsc).first()

    def resolve_branches_by_bank(self, info, bank_name):
        return BranchModel.query.join(BankModel).filter(BankModel.name == bank_name).all()

schema = graphene.Schema(query=Query)
