from brownie import FundMe, network
from scripts.helpful_script import get_account

def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy("0x8A753747A1Fa494EC906cE90E9f37563A8AF630e",{"from":account})
    # print(f"Contract deployed to {fund_me.address}")

def main():
    deploy_fund_me()