<template>
  <div class="grey">
    <!--面包屑-->
    <el-row>
      <el-col :span="18" :offset="3" class="breedCrumb">
        <el-breadcrumb separator="/">
          <el-breadcrumb-item :to="{ path: '/index/pets' }">萌宠园</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/index/pets/'+this.$route.params.id}"> 宠物详情</el-breadcrumb-item>
          <el-breadcrumb-item>我要领养</el-breadcrumb-item>
        </el-breadcrumb>
      </el-col>
    </el-row>
    <!--主体部分-->
    <el-row>
      <el-col :span="18" :offset="3" class="main">
        <el-form  label-position="left" label-width="80px" ref="formRef" :rules="rules" :model="form" >
          <el-form-item label="萌宠简介">
            <el-input :placeholder=this.pet.title disabled></el-input>
          </el-form-item>
          <el-form-item label="联系人" prop="name">
            <el-input v-model="form.name" placeholder="王五"></el-input>
          </el-form-item>
          <el-form-item label="手机号" prop="phone">
            <el-input v-model="form.phone" placeholder="11888888888"></el-input>
          </el-form-item>
          <el-form-item label="我的地址" prop="address">
            <el-input v-model="form.address" placeholder="北京市海淀区北京交通大学家属楼XX号"></el-input>
          </el-form-item>
          <el-form-item label="QQ号码" prop="QQ">
            <el-input v-model="form.QQ" placeholder="QQ号，选填"></el-input>
          </el-form-item>
          <el-form-item label="微信号" prop="wechat">
            <el-input v-model="form.wechat" placeholder="微信号，选填"></el-input>
          </el-form-item>
          <el-form-item label="领养条件" prop="message">
            <el-input style="width: 700px;" :rows="7" type="textarea" v-model="form.message" placeholder="描述家中领养环境，领养能力等"></el-input>
          </el-form-item>
          <el-form-item >
            <el-button type="primary" @click="onSubmit"><font-awesome-icon class="icon" :icon="['fas', 'check']"></font-awesome-icon><span>提交</span></el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: '',
  data () {
    return {
      form: {
        username: '',
        petID: '',
        name: '',
        phone: '',
        email: '',
        address: '',
        QQ: '',
        wechat: ''
      },
      pet: {},
      rules: {
        name: [
          { required: true, message: '请输入姓名', trigger: 'blur' }
        ],
        phone: [
          { required: true, message: '请输入手机号', trigger: 'blur' },
          { min: 11, max: 11, message: '请输入正确的手机号（11位）', trigger: 'blur' }
        ],
        address: [
          { required: true, message: '请输入具体地址', trigger: 'blur' }
        ],
        message: [
          { required: true, message: '请输入您的领养条件。这一条尤为重要，是我们判断的初步依据', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    onSubmit () {
      this.$refs.formRef.validate(async valid => {
        console.log(valid)
        if (!valid) { return }
        const result = await this.$http.post('pets/adopt', this.form)
        console.log(result.data)
        if (result.data.status === 200) {
          this.$message.success(result.data.msg)
        } else if (result.data.status === 202) {
          this.$message.error(result.data.msg)
        } else {
          this.$message.error(result.data.msg)
        }
      })
    }
  },
  created () {
    this.$http.get('pets/' + this.$route.params.id)
      .then(res => {
        const data = res.data
        console.log(data)
        if (data.status === 200) {
          this.pet = data.pet
          this.form.petID = this.pet.id
          this.form.username = window.sessionStorage.getItem('username')
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
    .el-form-item {
      margin: 18px 30px;
      width: 500px;
      .el-button {
        background-color: #ff6735;
        color: #f1f2f4;
        border: 0px;
        span {
          font-size: 16px;
          margin-left: 10px;
        }
      }
    }
  }
</style>
