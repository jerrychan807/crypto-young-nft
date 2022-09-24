const express = require('express') // 引入express
const app =express()
app.use(express.static("../dist")) // 托管到dist目录(打包)

module.exports = app // 导出app实例
