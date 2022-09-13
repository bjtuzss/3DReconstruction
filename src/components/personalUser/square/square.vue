<template>
  <div>
    <header>
      <el-row>
        <el-col :md="24" :offset="0">
          <h2>在这儿，分享你的创造！！！</h2>
          <h3>---分享创造价值</h3>
        </el-col>
      </el-row>
    </header>

    <div class="main">
      <el-row>
        <el-col :md="22" :offset="1">
            <div class="content clearfix ">
                <ul >
                  <li v-for="(model,index) in this.models" :key="index" class="item-block shadow" @click="postDetailBtn(model. projectid)">
                    <div class="item-card">
                      <div class="item-main">
                        <a href="###" >
                          <img  :src="pics[index]"/>
                        </a>
                      </div>
                      <div class="item-info">
                        <div class="item-info1">
                          <span><strong>{{model.name}}</strong></span>
                          <span style="float:right">{{model.type}}</span>
                        </div>
                        <div class="item-info2">
                          <p>{{model.content}}</p>
                        </div>
                      </div>
                    </div>
                  </li>
                </ul>
            </div>
        </el-col>
      </el-row>
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
          content: '对DTU数据集中的SCAN1进行三维重建字数补丁字数补丁',
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
    postDetailBtn (id, name) {
      this.$router.push('/index/square/model/' + id)
      this.$http.get('square/models/display?projectid=' + id)
        .then(res => {
          if (res.data.success) {
            this.$router.push('/index/square/model/' + id)
          }
        }, error => console.log(error))
    }
  },
  created () {
    this.$http.get('http://127.0.0.1:5000//square/models/getAll')
      .then(res => {
        const data = res.data
        console.log(data)
        if (data.success) {
          this.models = data.msg
          for (var i = 0; i < this.models.length; i++) {
            this.$http.get('/workshop/pic?userid=' + this.models[i].userId +
            '&projectName=' + this.models[i].projectname, {
              responseType: 'blob'
            }).then(res => {
              const blob = new Blob([res.data], { type: 'image/jpeg' })
              const url = window.URL.createObjectURL(blob)
              this.pics.push(url)
            })
          }
          this.models = tempList
        }
      }, error => console.log(error))
  }

}
</script>

<style lang="less" scoped>
  header {
    overflow: hidden;
    background: url(../../../assets/images/square_bkg1.jpg) no-repeat center;
    background-size: cover;
    height: 450px;
    h2 {
      font-size: 35px;
      color: #fff;
      text-align: center;
      margin-top: 150px;
    }
    h3 {
      font-size: 25px;
      color: #fff;
      text-align: center;
      margin: 50px 0;
    }
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
    cursor: pointer;
  }

  /* model--card--begin */
  .item-block {
    width: 290px;
    height: 280px;
    // background-color: blue;
    padding: 8px;
    margin-left: 10px;
  }
  .item-block .shadow{
    box-shadow: 10px 10px 10px -4px rgba(0, 0, 0, .3);;
  }
  .item-block .item-card{
    width: 270px;
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
  }
</style>
