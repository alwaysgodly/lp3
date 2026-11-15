LP3 (410246) - Blockchain Practical Codes and Steps

Included:
C1 - Install/configure MetaMask and inspect Ether transaction costs.
C2 - Create/configure a wallet and perform a test cryptocurrency transaction.
C3 - Bank account Solidity contract: deposit, withdraw, display balance.
C4 - Student information Solidity contract: struct, array, fallback and gas/fees.

IMPORTANT SAFETY:
- Use a test network such as Sepolia and test ETH from a reputable faucet.
- Never share your Secret Recovery Phrase or private key.
- Never paste your real recovery phrase into websites, forms or chat.
- Do not use real funds or deploy these practice contracts on mainnet.

------------------------------------------------------------
C1 - METAMASK CONFIGURATION AND TRANSACTION COSTS
------------------------------------------------------------
1. Install MetaMask only from its official website: https://metamask.io/
2. Create a new wallet and securely back up the Secret Recovery Phrase offline.
3. Select a test network (for example, Sepolia). If it is not visible, enable test networks in MetaMask settings.
4. Obtain Sepolia test ETH from a faucet. Test ETH has no real monetary value.
5. Open MetaMask Activity and inspect a test transaction.
6. Record the transaction hash, gas limit, gas used, gas price and total fee.
7. Transaction fee is generally:
       Fee (ETH) = Gas Used x Effective Gas Price (in Gwei) / 1,000,000,000
8. Compare fees for different test transactions. Fees depend on network conditions and transaction complexity.

------------------------------------------------------------
C2 - CREATE WALLET AND PERFORM CRYPTO TRANSACTION
------------------------------------------------------------
1. Open MetaMask and create/configure a wallet.
2. Switch to Sepolia test network.
3. Copy your public wallet address.
4. Receive Sepolia test ETH from a faucet.
5. Click Send and enter another test wallet address you control.
6. Enter a small test ETH amount, review the estimated fee and confirm.
7. Open Activity and inspect the transaction status and hash.
8. Explain the roles of sender address, receiver address, amount, nonce, gas and transaction hash.

------------------------------------------------------------
C3 - BANK ACCOUNT SMART CONTRACT
------------------------------------------------------------
File: 1_BankAccount.sol

Functions:
- deposit(): accepts Ether and adds it to the account balance.
- withdraw(amount): owner withdraws the requested amount in wei.
- displayBalance(): returns the recorded balance in wei.

Remix deployment:
1. Visit https://remix.ethereum.org/
2. Create BankAccount.sol and paste the code.
3. Open Solidity Compiler; select compiler 0.8.20 or compatible 0.8.x.
4. Compile the contract.
5. Open Deploy & Run Transactions.
6. Select Injected Provider - MetaMask and connect to Sepolia.
7. Deploy and confirm the transaction in MetaMask.
8. Call deposit using the Value field (for example 0.001 Ether) and select unit Ether.
9. Call displayBalance to view balance in wei.
10. Call withdraw with an amount in wei that does not exceed the balance.
11. Check transaction details and gas fees in MetaMask / Sepolia explorer.

------------------------------------------------------------
C4 - STUDENT INFORMATION SMART CONTRACT
------------------------------------------------------------
File: 2_StudentInformation.sol

Concepts:
- Structure: Student stores roll number, name, age and department.
- Array: students stores multiple Student records.
- addStudent(): adds a student.
- getStudent(index): returns a student record.
- getStudentCount(): returns number of stored records.
- fallback(): executes for unmatched function calldata; payable.
- receive(): accepts plain Ether transfers with empty calldata.

Remix steps:
1. Create StudentInformation.sol and paste the code.
2. Compile with Solidity 0.8.20 or compatible 0.8.x.
3. Deploy to Sepolia using Injected Provider - MetaMask.
4. Call addStudent with values, e.g. 101, "Amit", 20, "Computer".
5. Call getStudentCount; expected result is 1.
6. Call getStudent with index 0 to view the record.
7. To test fallback, use low-level interaction / send a transaction with unmatched calldata to the contract.
8. To test receive, send test ETH with empty calldata to the contract address.
9. Inspect transaction gas used and fees in MetaMask or a Sepolia explorer.

NOTE:
- Solidity function arguments and balances use wei where specified.
- The student contract is a demonstration and does not include access control or duplicate-roll-number checks.
- The bank contract records the balance maintained through its deposit/withdraw functions.
