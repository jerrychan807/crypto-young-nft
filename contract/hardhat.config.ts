import {HardhatUserConfig} from 'hardhat/types';
import 'hardhat-deploy';
import 'hardhat-deploy-ethers';
import '@nomiclabs/hardhat-etherscan';

// const privateKey = process.env.PRIVATE_KEY;
// const endpoint = process.env.BSCTESTNET_URL;
// const etherscanKey = process.env.ETHERSCAN_KEY;

const config: HardhatUserConfig = {
    defaultNetwork: "hardhat",
    networks: {
        hardhat: {},
        rinkeby: {
            url: "",
            chainId: 4,
            gasPrice: 10000000000,
            // gas: 2100000,
            timeout: 30000,
            // accounts: [`0x${privateKey}`]
            accounts: [``]
        },
           polygon: {
            url: "https://polygon-rpc.com/",
            chainId: 137,
            // gasPrice: 10000000000,
            gas: 2100000,
            timeout: 30000,
            // accounts: [`0x${privateKey}`]
            accounts: [``]
        },
    },
    solidity: {
        version: '0.8.7',
        settings: {
            optimizer: {
                enabled: true,
                runs: 300,
            },
        },
    },
    etherscan: {
        apiKey: "",
    },
    namedAccounts: {
        deployer: '0xABe904f6A2661F36C8ABD3c5DBAEFF2C8214cAC7',
    },
    paths: {
        sources: 'contracts',
    },
    mocha: {
        timeout: 100000000
    },
};
export default config;
// module.exports = process.env.PRIVATE_KEY;
