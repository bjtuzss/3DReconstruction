<template>
  <el-container class="home-container">
    <!--头部-->
    <el-header>
      <el-menu
        :default-active="activeIndex"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b">
        <!--logo-->
        <div id="logo"><a href="#">3D Resturction</a></div>
        <!--导航栏-->
        <el-submenu index="5">
          <template slot="title">个人中心</template>
          <el-menu-item v-show="loginOrNot" index="5-1">工作台</el-menu-item>
          <el-menu-item v-show="loginOrNot" index="5-2">退出</el-menu-item>
          <el-menu-item v-show="!loginOrNot" index="5-3">立即登录</el-menu-item>
        </el-submenu>
        <el-menu-item index="4">联系我们</el-menu-item>
<!--        <el-menu-item index="3">交流论坛</el-menu-item>-->
        <el-menu-item index="2">模型广场</el-menu-item>
        <el-menu-item index="1">首页</el-menu-item>
      </el-menu>
    </el-header>
    <!--主体-->
    <el-main>
      <router-view></router-view>
      <div>
        <button @click="returnTop" id="btnTop" title="返回顶部"><font-awesome-icon  icon="rocket"/></button>
      </div>
    </el-main>
    <!--页尾-->
    <el-footer>
      一站式三维重建@创客
    </el-footer>
  </el-container>
</template>

<script>
// 当网页向下滑动 50px 出现"返回顶部" 按钮
window.onscroll = function () {
  scrollFunction()
}

function scrollFunction () {
  if (document.getElementById('btnTop')) {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 30) {
      document.getElementById('btnTop').style.display = 'block'
    } else {
      document.getElementById('btnTop').style.display = 'none'
    }
  }
}

export default {
  name: '',
  data () {
    return {
      activeIndex: '1',
      loginOrNot: false,
      token: window.sessionStorage.getItem('token')
    }
  },
  methods: {
    logout () {
      this.$confirm('是否要退出登录?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        window.sessionStorage.clear()
        this.$router.push('/')
        this.$router.go(0)
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消'
        })
      })
      // window.sessionStorage.clear()
      // this.$router.push('/')
      // this.$router.go(0)
      // this.$http.post('logout', { token: this.token })
      //   .then(res => {
      //     const data = res.data
      //     console.log(data)
      //     if (data.status === 200) {
      //       window.sessionStorage.clear()
      //       this.$router.push('/')
      //       this.$router.go(0)
      //     }
      //   }, error => console.log(error))
    },
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
      switch (keyPath[0]) {
        case '1':
          this.$router.push('/index/home')
          break
        case '2':
          this.$router.push('/index/square')
          break
        case '3':
          this.$router.push('/index/blog')
          break
        case '4':
          this.$router.push('/index/contract')
          break
        case '5':
          if (keyPath[1] === '5-2') {
            this.logout()
            break
          } else if (keyPath[1] === '5-1') {
            this.$router.push('/workshop')
            break
          } else if (keyPath[1] === '5-3') {
            this.toLogin()
            break
          } else {
            break
          }
      }
    },
    returnTop () {
      document.body.scrollTop = 0
      document.documentElement.scrollTop = 0
    },
    toLogin () {
      this.$router.push('/login')
      // this.$confirm('是否要跳转至登录页面?', '提示', {
      //   confirmButtonText: '确定',
      //   cancelButtonText: '取消',
      //   type: 'warning'
      // }).then(() => {
      //   this.$router.push('/login')
      // }).catch(() => {
      //   this.$message({
      //     type: 'info',
      //     message: '已取消'
      //   })
      // })
    }

  },
  created () {
    const flag = window.sessionStorage.getItem('username')
    if (!flag) {
      this.loginOrNot = false
    } else {
      this.loginOrNot = true
    }
  }
}
</script>

<style lang="less" scoped>
  .el-menu {
    .el-menu-item ,.el-submenu{
      float: right;
    }
    .el-menu-item:first-of-type {
      margin-right: 60px;
    }
  }

  #logo a {
    float: left;
    display: inline;
    font-weight: 700;
    font-size: 40px;
    color: #fff;
    text-shadow: 2px 5px 3px rgba(0, 0, 0, 0.06);
    padding: 3px 50px;
  }
  .el-footer {
    text-align: center;
    background-color: rgb(28, 29, 33);
    color: #fff;
    padding: 20px;
  }

  /*返回顶部*/
  #btnTop {
    display: none;
    position: fixed;
    bottom: 20px;
    right: 30px;
    z-index: 99;
    border: none;
    outline: none;
    background-color: #9F9F9F;
    color: white;
    cursor: pointer;
    padding: 10px;
    border-radius: 2px;
    transform: rotate(270deg);
  }
  #btnTop:hover {
    background-color: #9F9F9F;
    opacity: 0.5;
  }
</style>
