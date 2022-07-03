![CryptoYoungLogo](https://raw.githubusercontent.com/jerrychan807/imggg/master/image/CryptoYoungLogo.jpg)

---

# Online

![20220703202943](https://raw.githubusercontent.com/jerrychan807/imggg/master/image/20220703202943.png)

![20220704005920](https://raw.githubusercontent.com/jerrychan807/imggg/master/image/20220704005920.png)

- [头像生成器网站](http://199.255.96.224:3000/)
- [Opensea](https://opensea.io/collection/cryptoyoung-v2)
- [Free mint on Polygon Now](https://polygonscan.com/address/0xc1e8efe8d62b855c34009013a8d354d093f3e7f1#writeContract)

# SourceCode

| Folder  | description |
| --- | --- |
| vue-color-avatar | 前端 |
| contract | 合约源文件 |
| resource | nft资源 |
| tools | 批量生成图片脚本 |

# Install:

## SmartContract:

```bash
cd contract/
# 部署到polygon主网
yarn hardhat deploy --network polygon
# polygonscan验证
yarn hardhat verify --contract contracts/CryptoYoung.sol:CryptoYoung --constructor-args arguments.ts --network 
polygon YourContractAddress
```

...
...
(updating)

# Refs:

- [vue-color-avatar](https://github.com/Codennnn/vue-color-avatar)
- [0xmonkey开源头像拼图](https://0xmonkey.fullstack.run/89cf4c91-510b5ed-e14fcc8e-b1f1a176-0-0-0-b1425ffb)
