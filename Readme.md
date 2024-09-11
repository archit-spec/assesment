#TO TEST:
deployed at: http://144.24.132.202:5000/gql
## Query to fetch all banks
```graphql 
# Query to fetch all banks
query AllBanks {
  allBanks {
    edges {
      node {
        id
        name
      }
    }
  }
}

## Query to fetch all branches
query AllBranches {
  allBranches {
    edges {
      node {
        ifsc
        branch
        address
        city
        district
        state
        bankId
      }
    }
  }
}

## Query to fetch a specific branch by IFSC code
query GetBranch($ifsc: String!) {
  branch(ifsc: $ifsc) {
    ifsc
    branch
    address
    city
    district
    state
    bankId
  }
}

## Query to fetch branches by bank name
query GetBranchesByBank($bankName: String!) {
  branchesByBank(bankName: $bankName) {
    ifsc
    branch
    address
    city
    district
    state
    bankId
  }
}
```
