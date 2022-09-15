// const path = require('path')

module.exports = {
  lintOnSave: false,
  //   devServer: {
  //     contentBase: path.join(__dirname, 'public'),
  //     port: 8000,
  //     proxy: 'http://localhost:888'
  //   }
  devServer: {
    proxy: {
      // 配置跨域
      '/api': {
        target: 'http://43.143.151.191:888/',
        changOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
}
