<template>
  <div>
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/workshop' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>模型查看</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="main">
      <el-card class="box-card">
        <el-row>
          <el-col :md="24" >
              <div class="content clearfix ">
                <ul >
                  <li v-for="(model,index) in this.models" :key="index" class="item-block shadow" >
                    <div class="item-card">
                      <div class="item-main">
                        <a href="###" >
                          <img @click="postDetailBtn(model.id)" :src="pics[index]"/>
                        </a>
                      </div>
                      <div class="item-info">
                        <div class="item-info1">
                          <span><strong>{{model.name}}</strong></span>
                          <span style="float:right">{{model.type}}</span>
                        </div>
                        <div class="item-info2">
                          <p>{{model.description}}</p>
                          <i class="el-icon-share" style="font-size:20px;width: 20%;" @click="shareBtn(model.pro)"></i>
                        </div>
                      </div>
                    </div>
                  </li>
                </ul>
              </div>
          </el-col>
        </el-row>
      </el-card>
    </div>
  </div>
</template>

<script>
export default {
  name: '',
  data () {
    return {
      models: [
        {
          id: '1',
          name: 'scan1',
          type: '生活用品',
          share_username: 'TORO',
          description: '对DTU数据集中的SCAN1进行三维重建字数补丁字数补丁',
          pic: require('../../../assets/images/model_example.jpg')
        },
        {
          id: '2', name: '', type: '', share_username: '', content: '2', pic: ''
        },
        {
          id: '3', name: '', type: '', share_username: '', content: '2', pic: ''
        },
        {
          id: '4', name: '', type: '', share_username: '', content: '2', pic: ''
        },
        {
          id: '5', name: '', type: '', share_username: '', content: '2', pic: ''
        },
        {
          id: '6', name: '', type: '', share_username: '', content: '2', pic: ''
        }
      ],
      pics: []
    }
  },
  methods: {
    postDetailBtn (id) {
      this.$router.push('/index/square/model/' + id)
      this.$http.get('square/models/display?mid=' + id)
        .then(res => {
          const data = res.data
          console.log(data)
          if (data.status === 200) {
            this.$router.push('/index/square/model/' + id)
          }
        }, error => console.log(error))
    },
    shareBtn (projectName) {
      this.$confirm('是否要分享此模型到模型广场?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$http.post('http://127.0.0.1:5000/workshop/models/share', { userid: window.sessionStorage.getItem('username'), projectName: projectName })
          .then(res => {
            const data = res.data
            console.log(data)
            this.$message({
              type: 'success',
              message: '分享成功!'
            })
          }, error => console.log(error))
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消分享'
        })
      })
    }
  },
  created () {
    this.$http.get('http://127.0.0.1:5000/workshop/models/getAll?userid=' + window.sessionStorage.getItem('username'))
      .then(res => {
        const data = res.data
        console.log(data)
        if (data.success) {
          console.log(data.msg)
          this.models = data.msg
          for (var i = 0; i < this.models.length; i++) {
            console.log(this.models[i].imgdir + '/00000000.jpg')
            this.$http.get('/workshop/pic?userid=' + window.sessionStorage.getItem('username') +
            '&projectName=' + this.models[i].projectName, {
              responseType: 'blob'
            }).then(res => {
              const blob = new Blob([res.data], { type: 'image/jpeg' })
              const url = window.URL.createObjectURL(blob)
              this.pics.push(url)
            })
          }
        }
      }, error => console.log(error))
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
   .content{
    width: 100%;
    margin: 0 auto;
    background: #f5f5f5;
  }
  .sticky{
    position: sticky;
    top: 0;
    padding: 5px;
    float:right;
  }
  .content ul li{
    float: left;
  }

  /* model--card--begin */
  .item-block {
    width: 250px;
    height: 280px;
    // background-color: blue;
    padding: 8px;
    margin-left: 10px;
  }
  .item-block .shadow{
    box-shadow: 10px 10px 10px -4px rgba(0, 0, 0, .3);;
  }
  .item-block .item-card{
    width: 230px;
    height: 260px;
    background-color: rgb(255, 255, 255);
  }
  .item-block .item-card .item-main {
    width: 100%;
    height: 72%;
    padding: 10px;
    background-color: rgb(255, 255, 255);
  }
  .item-block .item-card .item-main img{
    width: 100%;
    height: 100%;
    background-color: pink;
    overflow: hidden;
    cursor: pointer;
  }
  .item-block .item-card .item-info {
    height: 28%;
    padding: 8px;
    color: #d1d1d1;
  }
  .item-block .item-card .item-info .item-info1 {
    height: 35%;
    padding: 1px;
    padding-left: 4px;
    padding-right: 4px;
    font-size: 12px;
    color: #d1d1d1;
  }
  .item-block .item-card .item-info .item-info2 {
    width: 100%;
    height: 65%;
    padding: 2px;
    font-size: 12px;
    overflow: hidden;
    background-color: rgb(255, 255, 255);
    color:#d1d1d1;
    border-top: 1px solid #f5f5f5;
    padding-top: 5px;
    p {
      float: left;
      width: 80%;
    }
    i {
      float: left;
      width: 20%;
    }
  }
</style>
