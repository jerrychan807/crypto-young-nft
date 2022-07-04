import {HardhatRuntimeEnvironment} from 'hardhat/types';
import {DeployFunction} from 'hardhat-deploy/types';

const func: DeployFunction = async function (hre: HardhatRuntimeEnvironment) {
  const {deployments, getNamedAccounts} = hre;
  const {deploy} = deployments;

  const {deployer} = await getNamedAccounts();

  await deploy('CryptoYoung', {
    from: deployer,
    args: ["https://raw.githubusercontent.com/jerrychan807/crypto-young-nft/main/resource/",2,1000,100],
    gasLimit: 50000,
    log: true,
  });
};
export default func;
func.tags = ['CryptoYoung'];
