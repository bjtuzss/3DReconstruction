<template>
  <div class="grey">
    <!--面包屑-->
    <el-row>
      <el-col :span="22" :offset="1" class="breedCrumb">
        <el-breadcrumb separator="/">
          <el-breadcrumb-item :to="{ path: '/index/square' }">模型广场</el-breadcrumb-item>
          <el-breadcrumb-item>模型详情</el-breadcrumb-item>
        </el-breadcrumb>
      </el-col>
    </el-row>
    <!--主体部分-->
    <el-row>
      <el-col :span="22" :offset="1" class="main">
        <h3>{{model.title}}</h3>
        <!--上半部分-->
        <el-row :gutter="10">
          <el-col :span="18">
            <div class="left">
              <div class="photo">
                <img :src="model.pic" alt="">
              </div>
            </div>
          </el-col>
          <el-col :span="6">
            <div class="right">
              <h4  style="color: #b76361"><font-awesome-icon class="icon" :icon="['fas', 'flag']"></font-awesome-icon>【免费查看下载模型】</h4>
              <h4><font-awesome-icon class="icon" :icon="['fas', 'clock']"></font-awesome-icon><span>发布时间：</span>{{model.time}}</h4>
              <h4><font-awesome-icon class="icon" :icon="['fas', 'address-card']"></font-awesome-icon><span>模型名称:</span>{{model.project_name}}</h4>
              <h4><font-awesome-icon class="icon" :icon="['fas', 'home']"></font-awesome-icon><span>用户:</span>{{model.share_username}}</h4>
              <h4 style="color: #ff6c3c;"><font-awesome-icon class="icon" :icon="['fas', 'location-arrow']"></font-awesome-icon>{{model.from}}></h4>
              <h4><font-awesome-icon class="icon" :icon="['fas', 'user']"></font-awesome-icon><span>类型：</span>{{model.type}}</h4>
              <h4><font-awesome-icon class="icon" :icon="['fas', 'phone']"></font-awesome-icon><span>联系电话：</span> {{model.phone}}</h4>
              <!-- <el-button type="primary" @click="handleBtn"><font-awesome-icon :icon="['fas', 'paw']"></font-awesome-icon><span>我想领养它</span></el-button> -->
            </div>
          </el-col>
        </el-row>
        <!--下半部分-->
        <el-row>
          <el-col :span="24">
            <div class="content">
              <h3>详细描述</h3>
              <p>{{model.desc}}</p>
              <!-- <span class="alert"><font-awesome-icon class="icon" :icon="['fas', 'exclamation-triangle']"></font-awesome-icon>安全提示：请不要相信任何需要金钱交易的无偿领养！例如宠物免费，骗取运费等常见骗术！</span> -->
            </div>
          </el-col>
        </el-row>
      </el-col>
      <!-- <el-col :span="4">
        <div class="ad">
          <img src="../../../assets/images/ad.png" alt="">
        </div>
      </el-col> -->
    </el-row>
  </div>
</template>

<script>
export default {
  name: '',
  data () {
    return {
      model: {
        project_name: 'scan1',
        time: '2022-08-04',
        share_username: 'toro180',
        type: '文物',
        desc: 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
      }
    }
  },
  methods: {
    handleBtn () {
      const tokenStr = window.sessionStorage.getItem('token')
      if (!tokenStr) {
        this.$confirm('使用领养功能需要先登录。是否要跳转至登录页面?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$router.push('/login')
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消'
          })
        })
      } else {
        this.$router.push('/index/pets/' + this.$route.params.id + '/adopt')
      }
    }
  },
  created () {
    this.$http.get('pets/' + this.$route.params.id)
      .then(res => {
        const data = res.data
        console.log(data)
        if (data.status === 200) {
          this.pet = data.pet
          this.pet.pic = require('../../../assets/images/pet' + data.pet.pic + '.jpg')
        }
      }, error => console.log(error))
  }
}
</script>

<style lang="less" scoped>
  .grey {
    background-color: #f1f2f4;
  }
  .breedCrumb{
    .el-breadcrumb{
      background-color: #ffffff;
      font-size: 23px;
      margin: 5px 0;
      padding: 15px;
    }

  }
  .main {
    background-color: #ffffff;
    h3 {
      color: #999999;
      margin: 15px;
    }
    .left {
      display: flex;
      height:480px;
      border: 2px solid #e2e2e2;
      border-radius: 8px;
      overflow: visible;
      justify-content: center;
      align-items: center;
      margin: 15px;
      .photo {
        width: 80%;
        height: 96%;
        overflow: hidden;
        img {
          width: 100%;
        }
      }
    }
    .right {
      margin: 15px;
      height: 480px;
      /*background-color: pink;*/
      h4 {
        padding: 8px;
        h4 {
          float: right;
          background-color: #f0ad4e;
          border-radius: 1px;
          color: #ffffff;
          padding: 2px 8px;
        }
        span {
          display: inline-block;
          width: 80px;
          // background-color: #ff0000;
          // margin-right: 40px;
        }
      }
      .icon {
        margin-right: 15px;
        color: #f07057;
      }
      .el-button{
        margin: 10px;
        span{
          margin-left: 10px;
          font-size: 17px;
        }
      }
    }
    .content {
      margin: 10px 15px;
      border-left:2px solid #f0ad4e;
      padding: 20px 10px;
      .alert {
        display: inline-block;
        margin-top: 20px;
        color: #ff0000;
      }
    }
  }
  .ad{
    background-color: pink;
    margin-left: 10px;
    img{
      width: 100%;
    }
  }

</style>
