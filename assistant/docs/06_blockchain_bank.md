# FinNova Wallet: Blockchain Bank

## What it is
FinNova includes a bank built as a smart contract, called FinNovaBank, deployed on the Sepolia test network of Ethereum. It lets customers deposit, withdraw, transfer and check balances in test ether. Sepolia ether has no real value.

## Contract functions
- `deposit()`: send ether into your bank balance.
- `withdraw(amount)`: take ether from your balance back to your wallet. You cannot withdraw more than your balance.
- `transfer(to, amount)`: move part of your balance to another address inside the bank.
- `checkBalance()`: read your own balance.
- `balanceOf(address)`: read the balance of any address.
- `totalDeposits()`: read the total ether held by the bank.

The contract emits the events Deposited, Withdrawn and Transferred, which appear in the Blockchain page history and on the block explorer.

## Using it in the FinNova website
1. Open the Blockchain page in the FinNova website in a desktop browser with the MetaMask extension, or in the browser inside the MetaMask mobile app.
2. Connect MetaMask and switch to the Sepolia network.
3. Enter the FinNovaBank contract address and choose Use this contract.
4. Deposit, withdraw, transfer or check balance. MetaMask asks you to confirm every transaction.

## Android app limitation
MetaMask only injects its connection (`window.ethereum`) into a desktop browser with the extension or into MetaMask mobile's own browser. It is not available inside the FinNova Android app, so the Blockchain page cannot connect to a wallet there. Open the FinNova website in the MetaMask mobile app's Browser tab, on the Sepolia network, to use it from a phone.

## Safety
- FinNova never asks for your seed phrase or MetaMask password.
- Confirm each transaction in MetaMask yourself and check the amount and the network (Sepolia).
- Gas fees on Sepolia are paid in free test ether.
