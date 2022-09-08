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
<!--          <el-upload-->
<!--            class="upload-demo"-->
<!--            action="http://127.0.0.1:5000/workshop/images/upload"-->
<!--            :on-preview="handlePreview"-->
<!--            :on-remove="handleRemove"-->
<!--            :before-remove="beforeRemove"-->
<!--            multiple-->
<!--            :on-change="handleChange"-->
<!--            :on-exceed="handleExceed"-->
<!--            :file-list="fileList">-->
            <el-upload
              class="upload-demo"
              :show-file-list="false"
              action="http://127.0.0.1:5000/workshop/images/upload"
              name="file"
              multiple
              :data="file_info"
              :on-success="file_upload"
              :on-preview="handlePreview"
              :on-remove="handleRemove"
              :before-remove="beforeRemove"
              :on-exceed="handleExceed"
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
import { Message } from 'element-ui'

export default {
  name: 'inforInput',
  data () {
    return {
      fileList: [],
      form: {
        id: 2,
        project_name: 'scan1',
        type: '文物',
        pic: '0',
        desc: '巴拉巴拉',
        fileList: [
        ],
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
          { required: true, message: '请输入简述，该项为必填', trigger: 'blur' }
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
      console.log(this.fileList)
      const result = await this.$http.post('http://127.0.0.1:5000/workshop/project/create', this.form)
      console.log(result.data)
      if (result.data.success) {
        console.log(result.data.msg)
        this.$message.success(result.data.msg)
        this.form = {}
      } else {
        this.$message.error(result.data.msg)
      }
    },
    file_upload (resp) {
      if (resp.msg === '保存文件成功') {
        this.form.file_path = resp.filePath
        Message({
          message: resp.msg,
          type: 'success',
          duration: 5 * 1000
        })
      } else {
        Message({
          message: resp.msg,
          type: 'error',
          duration: 5 * 1000
        })
      }
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
</style>
