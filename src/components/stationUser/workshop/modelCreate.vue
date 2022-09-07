<template>
  <div>
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/workshop' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>模型创建</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card class="box-card">
      <el-form  label-position="left" label-width="80px" ref="formRef" :rules="rules" :model="form" >
        <el-form-item label="项目名称" prop="project_name">
          <el-input v-model="form.project_name"></el-input>
        </el-form-item>
        <el-form-item label="种类" prop="type">
          <el-input v-model="form.type"></el-input>
        </el-form-item>
        <el-form-item label="简述" prop="desc">
          <el-input type="textarea" v-model="form.desc" ></el-input>
        </el-form-item>
        <el-form-item label="图片上传" prop="pic">
          <el-upload
            class="upload-demo"
            action="http://127.0.0.1:5000/upload"
            ref="upload"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :before-remove="beforeRemove"
            :beforeUpload="beforeAvatarUpload"
            :limit="1"
            :data="maxID"
            :on-exceed="handleExceed"
            :on-change="handleChange"
            :file-list="form.fileList"
            :auto-upload="true"
          >
            <el-button size="small" type="primary">点击上传</el-button>
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
          </el-upload>
        </el-form-item>
        <el-form-item >
          <el-button type="primary" @click="onSubmit">提交</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'inforInput',
  data () {
    return {
      maxID: {
        maxID: '100'
      },
      form: {
        id: 2,
        project_name: 'scan1',
        type: '文物',
        pic: '0',
        desc: '巴拉巴拉',
        fileList: [
        ]
      },
      rules: {
        project_name: [
          { required: true, message: '请输入名字，该项为必填', trigger: 'blur' }
        ],
        type: [
          { required: true, message: '请输入模型所属种类，该项为必填', trigger: 'blur' }
        ],
        pic: [
          { required: true, message: '请上传图片，该项为必填', trigger: 'blur' }
        ],
        desc: [
          { required: true, message: '请输入简述，该项为必填', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    async getMaxID () {
      const result = await this.$http.get('home/petsInforInput/getMaxID')
      this.maxID.maxID = result.data
      console.log(result)
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    handleExceed (files, fileList) {
      this.$message.warning(`当前限制选择 1 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`)
    },
    handleChange (file, fileList) {
      console.log(file.name)
      this.getMaxID()
    },
    beforeRemove (file, fileList) {
      return this.$confirm(`确定移除 ${file.name}？`)
    },
    beforeAvatarUpload (file) {
      console.log(file.type)
      const isJPG = file.type === 'image/jpeg'
      // const isJPG = (file.type === 'image/jpeg' || file.type === 'image/png')
      const isLt2M = file.size / 1024 / 1024 < 2

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!')
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!')
      }
      return isJPG && isLt2M
    },
    onSubmit () {
      this.$refs.formRef.validate(async valid => {
        console.log(valid)
        if (!valid) { return }
        this.form.sid = window.sessionStorage.getItem('sid')
        console.log(this.form.fileList)
        // 上传图片
        // this.$refs.upload.submit()
        // 上传其他数据
        const result = await this.$http.post('workshop/project/create', this.form)
        console.log(result.data)
        if (result.data.status === 200) {
          console.log(result.data.msg)
          this.$message.success(result.data.msg)
          this.form = {}
        } else if (result.data.status === 202) {
          this.$message.error(result.data.msg)
        } else {
          this.$message.error(result.data.msg)
        }
      })
    }
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
