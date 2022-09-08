<template>
  <div class="login_container">
    <div class="login_box">
      <div class="avatar_box">
        <img src="../../../assets/images/pet1.jpg" alt="">
      </div>
      <!--      登录表单区域-->
      <div class="login_info" v-show="flag==0">
        <el-form :model="loginForm" :rules="rules" ref="loginFormRef" class="clearfix">
          <el-form-item prop="username">
            <el-input v-model="loginForm.username" placeholder="请输入用户名" prefix-icon="el-icon-user-solid"></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input v-model="loginForm.password" placeholder="请输入密码" prefix-icon="el-icon-key" type="password"></el-input>
          </el-form-item>
          <el-form-item class="btns">
            <el-button type="primary" @click="login">登录</el-button>
            <el-button type="info" @click="reset">重置</el-button>
          </el-form-item>
        </el-form>
        <el-link type="info" @click="registerPage">没有账号？立即注册</el-link>
        <el-link type="info" @click="stationPage">救助站登陆注册入口  /</el-link>
      </div>
      <!--      注册表单区域-->
      <div class="register_info" v-show="flag==1">
        <el-form :model="registerForm" :rules="rules" ref="registerFormRef" class="clearfix">
          <el-form-item prop="username">
            <el-input v-model="registerForm.username" placeholder="请输入2-15位用户名" prefix-icon="el-icon-user-solid"></el-input>
          </el-form-item>
          <el-form-item prop="password1">
            <el-input v-model="registerForm.password1" placeholder="请输入6-20位密码" prefix-icon="el-icon-key" type="password"></el-input>
          </el-form-item>
          <el-form-item prop="password2">
            <el-input v-model="registerForm.password2" placeholder="请重复输入密码" prefix-icon="el-icon-key" type="password"></el-input>
          </el-form-item>
          <el-form-item class="btns">
            <el-button type="primary" @click="register">立即注册</el-button>
            <el-button type="info" @click="reset">重置</el-button>
          </el-form-item>
        </el-form>
        <el-link type="info" @click="loginPage">已有账号？返回登录</el-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login',
  data () {
    const validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.registerForm.password1 !== '') {
          this.$refs.registerFormRef.validateField('password2')
        }
        callback()
      }
    }
    const validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.registerForm.password1) {
        console.log(1)
        callback(new Error('两次输入密码不一致!'))
      } else {
        console.log(value)
        callback()
      }
    }
    return {
      loginForm: {
        username: '',
        password: ''
      },
      registerForm: {
        username: '',
        password1: '',
        password2: ''
      },
      flag: 0,
      rules: {
        username: [
          { required: true, message: '请输入用户名称', trigger: 'blur' },
          { min: 2, max: 15, message: '长度在 2 到 15 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 20, message: '长度在 6 到 20 个字符', trigger: 'blur' }
        ],
        // 自定义检测
        password1: [
          { validator: validatePass, trigger: 'blur' },
          { min: 6, max: 20, message: '长度在 6 到 20 个字符', trigger: 'blur' }
        ],
        password2: [
          { validator: validatePass2, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    reset () {
      console.log(this)
      if (this.flag === 0) { this.$refs.loginFormRef.resetFields() } else {
        this.$refs.registerFormRef.resetFields()
      }
    },
    login () {
      // 方法一  async异步 await 等待
      this.$refs.loginFormRef.validate(async valid => {
        if (!valid) { return }
        window.sessionStorage.setItem('username', this.loginForm.username)
        const result = await this.$http.post('/user/login', this.loginForm)
        if (result.data.success) {
          window.sessionStorage.setItem('token', result.data.token)
          window.sessionStorage.setItem('username', this.loginForm.username)
          console.log(result.data.msg)
          this.$message.success(result.data.msg)
          await this.$router.push('/index/home')
        } else {
          this.$message.error(result.data.msg)
        }
      })
    },
    register () {
      this.$refs.registerFormRef.validate(async valid => {
        if (!valid) { return }
        const result = await this.$http.post('/user/register', this.registerForm)
        console.log(result)
        if (result.data.success) {
          console.log(result.data.msg)
          this.$message.success(result.data.msg)
          this.loginPage()
        } else {
          this.$message.error(result.data.msg)
        }
      })
    },
    registerPage () {
      this.flag = 1
      this.reset()
    },
    loginPage () {
      this.flag = 0
    },
    stationPage () {
      this.$router.push('/station')
    }
  }
}
</script>

<style lang="less" scoped>
  .login_container {
    background-color: #2b4b6b;
    height: 100%;
  }
  .login_box {
    position: relative;
    width: 450px;
    height: 345px;
    background-color: #fff;
    border-radius: 3px;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
  }
  .avatar_box {
    height: 130px;
    width: 130px;
    border: 1px solid #eee;
    border-radius: 50%;
    box-shadow: 0 0 10px #ddd;
    position: absolute;
    transform: translate(-50%,-50%);
    left: 50%;
    background-color: #fff;
    img {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background-color: #eee;
    }
  }
 .login_info ,.register_info {
    position: absolute;
    /*bottom: 0;*/
    top: 80px;
    width: 100% ;
    padding: 0 20px;
    .el-link {
      float: right;
      margin-top: -10px;
      margin-bottom: 10px;
      margin-left: 5px;
    }
   .btns {
     float: right;
   }
  }

</style>
