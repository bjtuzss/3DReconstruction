<template>
  <el-container class="container">
    <el-header>
      <div>
        <span class="favicon">3D Resturction</span>
        <span class="title">我的工作台</span>
      </div>
      <el-button type="info" @click="quitBtnHandle">退出</el-button>
    </el-header>
    <el-container>
      <el-aside width="200px">
        <el-menu
          background-color="#333744"
          text-color="#fff"
          active-text-color="#ffd04b"
          router
        >
          <el-menu-item index="/workshop/modelCreate">
            <i class="el-icon-notebook-2"></i>
            <span slot="title">创建</span>
          </el-menu-item>
          <el-menu-item index="/workshop/modelSpace">
            <i class="el-icon-reading"></i>
            <span slot="title">模型空间</span>
          </el-menu-item>
          <!-- <el-menu-item index="/base/StationInformation">
            <i class="el-icon-document"></i>
            <span slot="title">救助站资料修改</span>
          </el-menu-item> -->
        </el-menu>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: '',
  methods: {
    quitBtnHandle () {
      this.$router.push('/index/home')
    }
  }
}
</script>

<style lang="less" scoped>
  .container {
    height: 100%;
  }
  .el-header {
    background-color: #373d41;
    display: flex;
    justify-content: space-between;
    align-items: center;
    .favicon{
      font-weight: 700;
      font-size: 40px;
      color: #fff;
      text-shadow: 2px 5px 3px rgba(0, 0, 0, 0.06);
      padding: 3px;
    }
    .title {
      color: #ffffff;
      margin-left: 8px;
      font-size: 23px;
    }
  }
  .el-aside {
    background-color: #333744;
  }
  .el-main {
    /*background-color: #eaedfe;*/
    background-color: #f1f2f4;
  }
</style>
