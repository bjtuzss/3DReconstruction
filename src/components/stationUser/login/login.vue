<template>
    <div class="login_box">
      <div class="avatar_box">
        <img src="../../../assets/images/pet3.jpg" alt="">
      </div>
      <div class="login_info">
        <el-form :model="loginForm" :rules="rules" ref="loginFormRef" class="clearfix">
          <el-form-item prop="phone">
            <el-input v-model="loginForm.phone" placeholder="请输入手机号" prefix-icon="el-icon-user-solid"></el-input>
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
      </div>
    </div>
</template>

<script>
export default {
  name: '',
  data () {
    return {
      loginForm: {
        phone: '12345678912',
        password: '123456'
      },
      rules: {
        phone: [
          { required: true, message: '请输入手机号', trigger: 'blur' },
          { min: 11, max: 11, message: '请输入正确的手机号（11位）', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 20, message: '长度在 6 到 20 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    reset () {
      console.log(this)
      this.$refs.loginFormRef.resetFields()
    },
    login () {
      this.$refs.loginFormRef.validate(async valid => {
        console.log(valid)
        if (!valid) { return }
        const result = await this.$http.post('home/login', this.loginForm)
        console.log(result.data)
        if (result.data.status === 200) {
          // window.sessionStorage.setItem('token', result.data.token)
          window.sessionStorage.setItem('sid', result.data.sid)
          console.log(result.data.msg)
          this.$message.success(result.data.msg)
          this.$router.push('/base/petsInforInput')
        } else if (result.data.status === 202) {
          this.$message.error(result.data.msg)
        } else {
          this.$message.error(result.data.msg)
        }
      })
    },
    registerPage () {
      this.$router.push('/station/register')
    }
  }
}
</script>

<style lang="less" scoped>
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
  .login_info {
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
