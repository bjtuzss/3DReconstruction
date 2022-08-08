<template>
  <div class="login_box">
    <div class="avatar_box">
      <img src="../../../assets/images/pet3.jpg" alt="">
    </div>
    <!--      注册表单区域-->
    <div class="register_info" >
      <el-form :model="registerForm" :rules="rules" ref="registerFormRef" class="clearfix">
        <el-form-item prop="name">
          <el-input v-model="registerForm.name" placeholder="请输入2-15位救助站名" prefix-icon="el-icon-s-home"></el-input>
        </el-form-item>
        <el-form-item prop="address">
          <el-input v-model="registerForm.address" placeholder="请输入救助站所在地区" prefix-icon="el-icon-s-promotion"></el-input>
        </el-form-item>
        <el-form-item prop="owner">
          <el-input v-model="registerForm.owner" placeholder="请输入救助站所有者姓名" prefix-icon="el-icon-user-solid"></el-input>
        </el-form-item>
        <el-form-item prop="phone">
          <el-input v-model="registerForm.phone" placeholder="请输入手机号，此将作为你的账户登录账号" prefix-icon="el-icon-phone"></el-input>
        </el-form-item>
        <el-form-item prop="wechat">
          <el-input v-model="registerForm.wechat" placeholder="请输入微信号，选填" prefix-icon="el-icon-chat-round"></el-input>
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
</template>

<script>
export default {
  name: '',
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
      registerForm: {
        name: '海淀区宠物救助站',
        address: '海淀区',
        owner: '李四',
        phone: '12345678910',
        wechat: '',
        password1: '123456',
        password2: '123456'
      },
      rules: {
        name: [
          { required: true, message: '请输入救助站名称', trigger: 'blur' },
          { min: 2, max: 20, message: '长度在 2 到 20 个字符', trigger: 'blur' }
        ],
        address: [
          { required: true, message: '请输入救助站所在地', trigger: 'blur' },
          { min: 2, max: 20, message: '长度在 2 到 20 个字符', trigger: 'blur' }
        ],
        owner: [
          { required: true, message: '请输入救助站所有者姓名', trigger: 'blur' },
          { min: 2, max: 10, message: '长度在 2 到 10 个字符', trigger: 'blur' }
        ],
        phone: [
          { required: true, message: '请输入联系手机号', trigger: 'blur' },
          { min: 11, max: 11, message: '请输入正确的手机号（11）', trigger: 'blur' }
        ],
        // wechat: [
        //   { required: true, message: '请输入微信号', trigger: 'blur' }
        // ],

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
      this.$refs.registerFormRef.resetFields()
    },
    register () {
      this.$refs.registerFormRef.validate(async valid => {
        console.log(valid)
        if (!valid) { return }
        const result = await this.$http.post('home/register', this.registerForm)
        console.log(result.data)
        if (result.data.status === 200) {
          console.log(result.data.msg)
          this.$message.success(result.data.msg)
          this.$router.push('/station/login')
        } else if (result.data.status === 202) {
          this.$message.error(result.data.msg)
        } else {
          this.$message.error(result.data.msg)
        }
      })
    },
    loginPage () {
      this.$router.push('/station/login')
    }
  }
}
</script>

<style lang="less" scoped>
  .login_box {
    position: relative;
    width: 450px;
    height: 595px;
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
  .register_info {
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
