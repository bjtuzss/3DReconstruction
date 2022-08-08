<template>
  <el-row>
    <el-col :md="18" :offset="3">
      <div>
        <!--    发表博客-->
        <div class="adressBlog">
          <div class="title"><h2>撰写一个帖子</h2></div>
          <el-form :label-position="labelPosition" :rules="rules" label-width="80px" :model="postABlog" ref="adressBlogRef">
            <el-form-item label="标题" prop="title">
              <el-input v-model="postABlog.title"></el-input>
            </el-form-item>
            <el-form-item label="内容" prop="content">
              <el-input v-model="postABlog.content" type="textarea" :rows="7" ></el-input>
            </el-form-item>
            <el-form-item class="btns">
              <el-button type="primary" @click="address">发表</el-button>
              <el-button type="info" @click="clear">重置</el-button>
            </el-form-item>
          </el-form>
        </div>
        <!--    所有博客内容-->
        <div class="post-content">
          <h2>所有帖子</h2>
          <section v-for="(post,index) in posts" :key="post.id">
            <h3>{{post.title}}</h3>
            <font-awesome-icon class="likeBtn" :class="{red:like[index]}" icon="heart"   @click="current_id=post.id;like[index]=!like[index];handleLikeBtnClick()"/>
            <span class="likeNum">{{post.likes}}</span>
            <router-link :to="'/index/blog/'+post.id" >read more</router-link>
          </section>
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: 'blog',
  data () {
    return {
      current_id: 0,
      posts: [],
      like: [],
      labelPosition: 'left',
      postABlog: {
        title: '',
        content: '',
        token: window.sessionStorage.getItem('token')
      },
      rules: {
        title: [
          { required: true, message: '标题不能为空', trigger: 'blur' }
        ],
        content: [
          { required: true, message: '内容不能为空', trigger: 'blur' }
        ]
      }
    }
  },
  created () {
    this.$http.get('posts')
      .then(res => {
        const data = res.data
        console.log(data)
        if (data.status === 200) {
          this.posts = data.blogs
          for (var i = 0; i < this.posts.length; i++) {
            this.like[i] = false
          }
        }
      }, error => console.log(error))
  },
  methods: {
    address () {
      const flag = window.sessionStorage.getItem('username')
      if (!flag) {
        this.$confirm('发表博客需要先登录。是否要跳转至登录页面?', '提示', {
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
        this.$refs.adressBlogRef.validate(async valid => {
          console.log(valid)
          if (!valid) { return }
          this.$http.post('address', this.postABlog)
            .then(res => {
              const data = res.data
              console.log(data)
              if (data.status === 200) {
                this.post = data.post
              }
            }, error => console.log(error))
          this.$refs.adressBlogRef.resetFields()
          this.reload()
          return this.$message.success('发表成功')
        })
      }
    },
    clear () {
      console.log(this)
      this.$refs.adressBlogRef.resetFields()
    },
    reload () {
      this.isRouterAlive = false
      this.$nextTick(function () {
        this.isRouterAlive = true
      })
    },
    handleLikeBtnClick () {
      var index
      for (var i = 0; i < this.posts.length; i++) {
        if (this.posts[i].id === this.current_id) {
          index = i
          break
        }
      }
      if (this.like[index]) {
        this.$http.post('like', { op: '1', id: this.current_id })
          .then(res => {
            const data = res.data
            console.log(data)
            this.posts = data.blogs
          }, error => console.log(error))
      } else {
        this.$http.post('like', { op: '0', id: this.current_id })
          .then(res => {
            const data = res.data
            console.log(data)
            this.posts = data.blogs
          }, error => console.log(error))
      }
    }
  }
}
</script>

<style scoped>
  .adressBlog {
    /*background-color: rgb(236, 239, 200);*/
    background-color: rgb(180, 199, 231);
    border-radius: 8px;
    padding: 10px;
  }
  .title {
    margin: 20px 15px;
  }
  .post-content {
    margin-top: 15px;
  }
  h2 {
    margin: 20px 10px;
    font-size:1.5rem;
  }
  section {
    /*height: 87px;*/
    border-bottom: 1px solid rgba(0,0,0,.1);
  }
  h3 {
    font-size: 1.25rem;
    margin: 10px 0;
    font-weight:normal
  }
  a {
    display: block;
    font-size: 1rem;
    margin: 30px 10px;
  }
  .likeBtn {
    color: grey;
  }
  .likeBtn:hover {
    cursor: pointer;
  }
  .grey {
    color: grey;
  }
  .red {
    color: red;
  }
  .likeNum {
    margin-left: 15px;
  }

</style>
