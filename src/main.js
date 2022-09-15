import Vue from 'vue'
import './plugins/fontawesome'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import './assets/css/global.css'
import axios from 'axios'

Vue.config.productionTip = false
// 配置请求的根路径
axios.defaults.baseURL = 'http://127.0.0.1:5000'
// axios.defaults.headers.option['Content-Type'] = 'application/json;charset=utf-8'
// axios.interceptors.request.use(config => {
//   console.log(config);
//   if (config.method === 'options') {
//     config.headers.Authorization = 'Bearer' + store.state.token
//   }
// })
Vue.prototype.$http = axios

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')