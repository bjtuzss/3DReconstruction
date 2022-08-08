<template>
  <div>
    <!-- 轮播图-->
    <el-carousel indicator-position="outside" height="500px">
      <el-carousel-item v-for="(item,index) in boxs" :key="index">
        <div class="box">
          <el-row>
            <el-col :span="8" :offset="8"><h3>{{item.title}}</h3></el-col>
          </el-row>
          <el-row>
            <el-col :span="8" :offset="8">
              <div class="box-content" v-html="item.content">{{item.content}}</div>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="8" :offset="8"> <el-button type="info" round @click="goto(index)">read more</el-button></el-col>
          </el-row>
        </div>
      </el-carousel-item>
    </el-carousel>
    <div class="my-container">
      <!-- about1 -欢迎-->
      <div class="about1">
        <h3>Welcome to Our Website</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore
          magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
          consequat.</p>
        <p>客观世界的物体是三维的，而我们用摄像机获取的图像是二维的，但是我们可以通过二维图像感知目标的三维信息。三维重建技术是以一定的方式处理图像进而得到计算机能够识别的三维信息，由此对目标进行分析。</p>
        <img src="../../../assets/images/home2.jpg" alt="" class="img-fluid">
      </div>
      <!-- about2 -我们的工作-->
      <!-- <div class="about2">
        <h3>What we do</h3>
        <el-row>
          <el-col :md="4" v-for="(o,index) in wedos" :key="index" :offset="index = 3">
            <el-card :body-style="{ padding: '0px' }" shadow="never" >
              <img :src="o.img" class="image">
              <div style="padding: 14px;">
                <span class="card-title">{{o.title}}</span>
                <div class="card-content" v-html="o.content">{{o.content}}</div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div> -->
      <!-- about3 -重建流程-->
      <div class="about3">
        <h3>重建流程</h3>
        <h5>XXXXXXXXXXXXXXXXXXXXXXX</h5>
        <el-row>
          <el-col :md="4" v-for="(o,index) in flow" :key="index" :offset="index>0 ? 1:3">
            <el-card :body-style="{ padding: '0px' }" shadow="never">
              <img :src="o.img" class="image" style="height:165px">
              <div style="padding: 14px;">
                <div class="card-content" v-html="o.content">{{o.content}}</div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>
      <!-- about4 -联系我们-->
      <div class="about4">
        <h3>联系我们</h3>
        <h5>如有相关事宜，请按以下方式给我们留言，或上门造访。</h5>
        <el-row class="contactUs">
          <el-col :span="12" :offset="6">
            <el-row :gutter="40">
              <el-col :span="13">
                <el-form  :model="form">
                  <el-form-item>
                    <el-input v-model="form.name" placeholder="姓名"></el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-input v-model="form.email" placeholder="邮箱"></el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-input v-model="form.message" placeholder="留言"></el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-button type="primary" @click="onSubmit">提交</el-button>
                  </el-form-item>
                </el-form>
              </el-col>
              <el-col :span="11">
                <ul>
                  <li>
                    <font-awesome-icon :icon="['fas', 'home']"></font-awesome-icon>
                    <h5>北下关街道上园村3号16号楼</h5>
                  </li>
                  <li>
                    <font-awesome-icon :icon="['fas', 'phone']"></font-awesome-icon>
                    <h5>12345678987</h5>
                  </li>
                  <li>
                    <font-awesome-icon :icon="['fas', 'envelope']"></font-awesome-icon>
                    <h5>1097546295@qq.com</h5>
                  </li>
                </ul>
              </el-col>
            </el-row>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: '',
  data () {
    return {
      boxs: [
        {
          title: '进入三维重建',
          content: '<p>一键上传图片<br>在线分析---方便快捷 <br>支持手机拍摄图片---随时随地三维重建</p>'
        },
        {
          title: '模型广场',
          content: '<p>三维模型广场<br>分享您的三维模型---赠人玫瑰 <br>使用别人的分享---分享交流</p>'
        },
        {
          title: '欢迎进入交流论坛',
          content: '<p>交流你所热爱的<br>新手指南---快速上手 <br>技术分享---进一步提升</p>'
        },
        {
          title: '联系我们',
          content: '<p>问题反馈<br>反馈我们的不足---帮助我们 <br>亦或提出你的建议---分享交流</p>'
        }
      ],
      wedos: [
        {
          title: '收养流浪猫狗',
          content: '<p>我们的工作人员会定时去各个地方查看流浪猫狗的存在，只要我们发现了都会带回到我们的协会中心收养。</p>',
          img: require('../../../assets/images//wh1.jpg')
        }, {
          title: '健康的保障',
          content: '<p>收养进来的流浪猫狗，我们会帮助它们进行基本的驱虫和检查，并且保障它们良好的身体健康。</p>',
          img: require('../../../assets/images//wh2.jpg')
        }, {
          title: '帮助找新家',
          content: '<p>我们会给健康的流浪猫狗，找到适合它们的新家庭，领养人我们会经过严格的筛选，达到我们的条件才能成功的领养。</p>',
          img: require('../../../assets/images//wh3.jpg')
        }
      ],
      flow: [
        {
          title: '照片拍摄',
          content: '<p>推荐对重建物体进行360°环绕拍摄，并从上中下至少三个俯视角度进行拍摄，提高重建效果。</p>',
          img: require('../../../assets/images//step1.jpg')
        }, {
          title: '项目创建',
          content: '<p>进入工作台，创建项目并命名，然后上传拍摄的照片。</p>',
          img: require('../../../assets/images//step2.jpg')
        }, {
          title: '三维重建',
          content: '<p>上传照片后，云端服务器会立即开始重建，重建时间不等。</p>',
          img: require('../../../assets/images//step3.jpg')
        }, {
          title: '模型管理',
          content: '<p>重建完成后，可以在线浏览查看，可以下载使用，亦或分享到模型广场。</p>',
          img: require('../../../assets/images//step4.jpg')
        }
      ],
      form: {
        email: '',
        name: '',
        message: ''
      }
    }
  },
  methods: {
    goto (index) {
      switch (index) {
        case 0:
          this.$router.push('/index/home')
          break
        case 1:
          this.$router.push('/index/pets')
          break
        case 2:
          this.$router.push('/index/blog')
          break
        case 3:
          this.$router.push('/index/contract')
          break
      }
    },
    onSubmit () {
      this.$http.post('visitorMessage', this.form)
        .then(res => {
          const data = res.data
          console.log(data)
          if (data.status === 200) {
            this.$message.success(res.data.msg)
          }
        }, error => console.log(error))
    }
  }
}
</script>

<style lang="less" scoped>
  /*轮播图*/
  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }
  .el-carousel__item:nth-of-type(1) {
    background: url(../../../assets/images/bkg7.jpg) no-repeat center;
    background-size: cover;
  }
  .el-carousel__item:nth-of-type(2) {
    background: url(../../../assets/images/square_bkg1.jpg) no-repeat center;
    background-size: cover;
  }
  .el-carousel__item:nth-of-type(3) {
    background: url(../../../assets/images/bkg6.jpg) no-repeat center;
    background-size: cover;
  }
  .el-carousel__item:nth-of-type(4) {
    background: url(../../../assets/images/bkg2.jpg) no-repeat center;
    background-size: cover;
  }
  .el-carousel {
    .el-row {
      text-align: center;
      margin: 20px 0;
      h3 {
        font-size: 48px;
        color: #fff;
        margin: 0 auto;
        text-align: center;
      }
      .box-content{
        margin-top: -40px;
        font-size: 18px;
        color: #fff;
      }
    }
  }
  /*about1*/
  .about1, .about2,.about3, .about4{
    text-align: center;
    margin: 70px 0;
    h3 {
      font-size: 42px;
      font-weight: bold;
    }
    h5 {
      font-size: 22px;
      color: #555555;
      margin-top: 18px;
      font-weight: inherit;
    }
    p {
      font-size: 15px;
      color: #999;
      margin: 10px 200px;
    }
  }
  .about2 {
    img {
      border-radius: 50%;
    }
    .el-card {
      margin-top: 30px;
      border:0;
      overflow: visible;
      .card-title {
        font-size: 25px;
        color: #222222;
      }
      .card-content {
        width: 200px;
        font-size: 15px;
        margin-top: 15px;
        color:#50555c
      }
    }
  }
  .about3 {
    img {
      width: 100%;
    }
    .el-card {
      margin-top: 30px;
      border:0;
      overflow: visible;
      .card-content {
        width: 200px;
        font-size: 16px;
        margin-top: 15px;
        color:#50555c
      }
    }
  }
  .about4 {
    .contactUs {
      text-align: left;
      margin:50px 0;
      ul li h5{
        display: inline-block;
        margin: 0 0 20px 10px;
      }
    }
  }
</style>
