<template>
  <div>
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/base' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path:'/base/petsInfor'}">宠物信息查看</el-breadcrumb-item>
      <el-breadcrumb-item>宠物领养请求</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card class="box-card">
      <ul>
        <li class='box' v-for="(item,index) in this.requests" :key="index">
          <ul class="clearfix">
            <li>创建时间：{{item.time}}</li>
            <li>用户：{{item.user}}</li>
            <li>联系人：{{item.name}}</li>
            <li>手机号：{{item.phone}}</li>
            <li>地址：{{item.address}}</li>
            <li>简介：{{item.content}}</li>
            <li class="tip">
              路过协商好后，请点击确认，平台会对送养记录进行记录
              <el-button type="warning" @click="confirmHandle(item.user)">确认</el-button>
            </li>
          </ul>
        </li>
      </ul>
      <div v-show="nullFlag">
        此宠物暂无领养请求
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: '',
  data () {
    return {
      nullFlag: false,
      id: '',
      requests: [
        {
          id: 1
        }
      ]
    }
  },
  methods: {
    async confirmHandle (data) {
      const result = await this.$http.post('/home/pets/adoptConfirm', { id: this.id, user: data })
      this.$message.success(result.data.msg)
    },
    getRequests () {
      this.$http.get('home/pets/' + this.$route.params.id + '/adoptCheck')
        .then(res => {
          const data = res.data
          console.log(data)
          if (data.status === 200) {
            this.requests = data.request
            if (data.request.length === 0) {
              this.nullFlag = true
            } else {
              this.nullFlag = false
            }
          }
        }, error => console.log(error))
    }
  },
  created () {
    this.id = this.$route.params.id
    this.getRequests()
  }
}
</script>

<style lang="less" scoped>
  .el-breadcrumb {
    font-size: 18px;
    margin-bottom: 15px;
  }
  .el-card {
    box-shadow: 0 1px 1px rgba(0,0,0,0.15);
  }
  .box {
    border: 2px solid #f1f2f4;
    padding: 17px;
    margin: 20px;
    li {
      margin: 10px;
    }
    .tip {
      float: right;
      margin-right:20px;
      color: rgb(255, 132, 107);
    }
  }
</style>
