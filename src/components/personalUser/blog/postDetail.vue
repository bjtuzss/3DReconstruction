<template>
  <div class="blog-detail">
    <header>
      <el-row>
        <el-col :md="24" :offset="0">
          <h2>在这儿，你可以找到志同道合的朋友，发现萌宠圈的知识！！</h2>
          <h3>---加入我们！</h3>
        </el-col>
      </el-row>
    </header>

    <el-row>
      <el-col :md="18" :offset="3">
        <div class="main">
          <h1>{{post.title}}</h1>
          <div class="content">
            {{post.content}}
          </div>
        </div>
        <div class="footer">
          <h5>作者：{{post.username}}</h5>
        </div>

      </el-col>
    </el-row>
  </div>

</template>

<script>
export default {
  name: 'postDetail',
  data () {
    return {
      post: {},
      comments: [],
      showCommentBox: false
    }
  },
  created () {
    this.$http.get('posts/' + this.$route.params.id)
      .then(res => {
        const data = res.data
        console.log(data)
        if (data.status === 200) {
          this.post = data.post
        }
      }, error => console.log(error))
  }
}
</script>

<style lang="less" scoped>
  .blog-detail {
    header {
      overflow: hidden;
      background: url(../../../assets/images/background3.jpg) no-repeat center;
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
    .main {
      h1 {
        text-align: center;
        font-size: 40px;
      }
    }
    .content {
      margin: 20px 0;
    }
    .footer {
      h5 {
        float: right;
        font-size: 16px;
      }
    }
  }

</style>
