<template>
  <div>
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/base' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>救助站资料修改</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card class="box-card">
      <el-form  label-position="right" label-width="80px" ref="formRef" :rules="rules" :model="form" >
        <el-form-item >
          <el-button type="warning" @click="ifModifyHandle" :disabled="flag" v-show="!flag"><span>点击开始修改救助站资料</span></el-button>
        </el-form-item>
        <el-form-item label="救助站名" prop="sname">
          <el-input v-model="form.sname" placeholder="海淀区救助站" :disabled="!flag"></el-input>
        </el-form-item>
        <el-form-item label="联系人" prop="sowner">
          <el-input v-model="form.sowner" placeholder="王五" :disabled="!flag"></el-input>
        </el-form-item>
        <el-form-item label="手机号" prop="sphone">
          <el-input v-model="form.sphone" placeholder="11888888888" :disabled="!flag"></el-input>
        </el-form-item>
        <el-form-item label="我的地址" prop="saddress">
          <el-input v-model="form.saddress" placeholder="北京市海淀区北京交通大学家属楼XX号" :disabled="!flag"></el-input>
        </el-form-item>
        <el-form-item label="微信号" prop="swechat">
          <el-input v-model="form.swechat" placeholder="微信号" :disabled="!flag"></el-input>
        </el-form-item>
        <el-form-item label="登录密码" prop="spassword">
          <el-input type='password' v-model="form.spassword" placeholder="密码" :disabled="!flag"></el-input>
        </el-form-item>
        <el-form-item >
          <el-button type="primary" @click="onSubmit" :disabled="!flag"><font-awesome-icon class="icon" :icon="['fas', 'check']" ></font-awesome-icon><span>提交</span></el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
export default {
  name: '',
  data () {
    return {
      flag: false,
      form: {
        sname: '',
        saddress: '',
        sowner: '',
        sphone: '',
        swechat: '',
        spassword: ''
      },
      rules: {
        sname: [
          { required: true, message: '请输入救助站名称', trigger: 'blur' },
          { min: 2, max: 20, message: '长度在 2 到 20 个字符', trigger: 'blur' }
        ],
        saddress: [
          { required: true, message: '请输入救助站所在地', trigger: 'blur' },
          { min: 2, max: 20, message: '长度在 2 到 20 个字符', trigger: 'blur' }
        ],
        sowner: [
          { required: true, message: '请输入救助站所有者姓名', trigger: 'blur' },
          { min: 2, max: 10, message: '长度在 2 到 10 个字符', trigger: 'blur' }
        ],
        sphone: [
          { required: true, message: '请输入联系手机号', trigger: 'blur' },
          { min: 11, max: 11, message: '请输入正确的手机号（11）', trigger: 'blur' }
        ],
        spassword: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 20, message: '长度在 6 到 20 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    ifModifyHandle () {
      this.flag = !this.flag
    },
    onSubmit () {
      this.$refs.formRef.validate(async valid => {
        console.log(valid)
        if (!valid) { return }
        this.form.sid = window.sessionStorage.getItem('sid')
        const result = await this.$http.post('home/informationModify', this.form)
        console.log(result.data)
        if (result.data.status === 200) {
          console.log(result.data.msg)
          this.$message.success(result.data.msg)
          this.flag = false
        } else if (result.data.status === 202) {
          this.$message.error(result.data.msg)
        } else {
          this.$message.error(result.data.msg)
        }
      })
    }
  },
  created () {
    this.$http.get('home/informationGet/' + window.sessionStorage.getItem('sid'))
      .then(res => {
        const data = res.data
        console.log(data)
        if (data.status === 200) {
          this.form = data.form
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
    .el-form-item {
      width: 700px;
    }
  }
</style>
