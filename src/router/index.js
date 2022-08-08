import Vue from 'vue'
import VueRouter from 'vue-router'
// 普通用户
import Login from '../components/personalUser/login/login.vue'
import Home from '../components/personalUser/home/home.vue'
import Index from '../components/personalUser/index.vue'
import Blog from '../components/personalUser/blog/blog.vue'
import PostDetail from '../components/personalUser/blog/postDetail'
import Square from '../components/personalUser/square/square'
import Contract from '../components/personalUser/contract/contractUs'
import ModelDetail from '../components/personalUser/square/modelDetail'
import MyCenter from '../components/personalUser/personalCenter/myCenter'
// 救助站用户
import Base from '../components/stationUser/workshop/base'
import StationHome from '../components/stationUser/workshop/home'
import ModelSpace from '../components/stationUser/workshop/modelSpace'
import ModelCreate from '../components/stationUser/workshop/modelCreate'
import StationInformation from '../components/stationUser/workshop/stationInformation'
import AdoptReq from '../components/stationUser/workshop/adoptReq'
import Base2 from '../components/stationUser/login/base2'
import StationLogin from '../components/stationUser/login/login'
import StationRegister from '../components/stationUser/login/register'

Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/index/home' },
  { path: '/login', component: Login },
  {
    path: '/index',
    component: Index,
    children: [
      { path: '/index/home', component: Home },
      { path: '/index/square', component: Square },
      { path: '/index/square/model/:id', component: ModelDetail },
      { path: '/index/blog', component: Blog },
      { path: '/index/blog/:id', component: PostDetail },
      { path: '/index/contract', component: Contract },
      { path: '/index/myCenter', component: MyCenter }
    ]
  },
  {
    path: '/workshop',
    component: Base,
    redirect: '/workshop/home',
    children: [
      { path: '/workshop/home', component: StationHome },
      { path: '/workshop/modelCreate', component: ModelCreate },
      { path: '/workshop/modelSpace', component: ModelSpace },
      { path: '/workshop/petsInfor/:id/adoptReq', component: AdoptReq },
      { path: '/workshop/StationInformation', component: StationInformation }
    ]
  },
  {
    path: '/station',
    component: Base2,
    redirect: '/station/login',
    children: [
      { path: '/station/login', component: StationLogin },
      { path: '/station/register', component: StationRegister }
    ]
  }
]

const router = new VueRouter({
  routes
})

// // 挂载路由导航守卫
// router.beforeEach((to, from, next) => {
//   if (to.path === '/login') return next()
//   // 获取token
//   const tokenStr = window.sessionStorage.getItem('token')
//   if (!tokenStr) return next('/login')
//   next()
// })
export default router
