<template>
  <div class="grey">
    <!--面包屑-->
    <el-row>
      <el-col :span="18" :offset="3" class="breedCrumb">
        <el-breadcrumb separator="/">
          <el-breadcrumb-item >个人中心</el-breadcrumb-item>
          <el-breadcrumb-item > 我的领养请求</el-breadcrumb-item>
        </el-breadcrumb>
      </el-col>
    </el-row>
    <!--主体部分-->
    <el-row>
      <el-col :span="18" :offset="3" class="main">
        <ul>
          <li class='box' v-for="(item,index) in informs" :key="index">
            <ul>
              <li>创建时间：{{item.time}}</li>
              <li>送养简介：{{item.briefInfo}}</li>
              <li>送养状态：{{item.state1==0 ? '未送养':'已送养'}}</li>
              <li>是否领养成功：{{item.state2==0 ? '否':'是'}}</li>
            </ul>
          </li>
        </ul>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: '',
  data () {
    return {
      informs: [
        {
          time: '2020-08-25 14:19:10',
          briefInfo: '2个月大中华田园犬',
          state1: 0,
          state2: 0
        }
      ]
    }
  },
  created () {
    const username = window.sessionStorage.getItem('username')
    this.$http.post('adoptReq', { username: username })
      .then(res => {
        const data = res.data
        console.log(data)
        if (data.status === 200) {
          this.informs = data.informs
        }
      }, error => console.log(error))
  }
}
</script>

<style lang="less" scoped>
  .grey {
    background-color: #f1f2f4;
    min-height: 550px;
  }
  .breedCrumb {
    .el-breadcrumb {
      background-color: #ffffff;
      font-size: 23px;
      margin: 5px 0;
      padding: 15px;
    }
  }

  .main {
  background-color: #ffffff;
    .box {
      border: 2px solid #f1f2f4;
      padding: 17px;
      margin: 20px;
      li {
        margin: 10px;
      }
    }
  }
</style>
