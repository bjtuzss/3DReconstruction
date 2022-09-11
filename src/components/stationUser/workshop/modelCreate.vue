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
          <el-input type="textarea" v-model="form.desc"></el-input>
        </el-form-item>
        <el-form-item label="图片上传" prop="pic">
          <el-upload
            class="upload-demo"
            accept=".jpeg,.png,.jpg,.bmp,.gif"
            :show-file-list="fileList"
            action="http://127.0.0.1:5000/workshop/images/upload"
            name="file"
            multiple
            :data="file_info"
            :before-upload="handleBefore"
            :on-success="file_upload"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :before-remove="beforeRemove"
            :on-exceed="handleExceed"
            v-bind:disabled="this.form.project_name === '' || this.form.type === '' "
          >
            <el-button size="small" type="primary" v-bind:disabled="this.form.project_name === '' || this.form.type === '' || this.form.fileList === []">点击上传</el-button>
            <div slot="tip" class="el-upload__tip">只能上传图片文件，且不超过500kb</div>
          </el-upload>
        </el-form-item>
        <el-form-item >
          <el-button type="primary" @click="onSubmit" v-bind:disabled="this.form.project_name === '' || this.form.type === '' ">提交</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import { Message } from 'element-ui'

export default {
  name: 'inforInput',
  data () {
    return {
      fileList: [],
      form: {
        username: window.sessionStorage.getItem('username'),
        project_name: '',
        type: '',
        pic: '',
        desc: '',
        fileList: [],
        file_path: ''
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
          { required: true, message: '请输入简述' }
        ]
      }
    }
  },
  computed: {
    file_info () {
      return {
        user_id: window.sessionStorage.getItem('username'),
        pro_name: this.form.project_name
      }
    }
  },
  methods: {
    async onSubmit () {
      const result = await this.$http.post('http://127.0.0.1:5000/workshop/project/create', this.form)
      if (result.data.success) {
        console.log(result.data.msg)
        this.$message.success(result.data.msg)
        this.form = {}
      } else {
        this.$message.error(result.data.msg)
      }
    },
    file_upload (resp) {
      if (resp.msg === '上传文件成功') {
        this.form.file_path = resp.filePath
        Message({
          message: resp.msg,
          type: 'success',
          duration: 1000
        })
      } else {
        Message({
          message: resp.msg,
          type: 'error',
          duration: 1000
        })
      }
    },
    handleBefore (file, fileList) {
      console.log(this.form.project_name)
      console.log(this.form.type)
      return new Promise((resolve, reject) => {
        if (this.form.project_name === '' || this.form.type === '') {
          this.$message.error('请先填写上述必选项')
          return reject(new Error('请先填写上述必选项'))
        }
        return resolve()
      })
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    handleExceed (files, fileList) {
      this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`)
    },
    beforeRemove (file, fileList) {
      return this.$confirm(`确定移除 ${file.name}？`)
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
  .upload-demo {
    max-height: 450px;
    //overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    -webkit-line-clamp: 10;
    -webkit-box-orient: vertical;
    display: -webkit-box;
    overflow: auto;
  }
</style>
