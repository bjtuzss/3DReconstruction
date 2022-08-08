<template>
 <div>
   <header>
     <el-row>
       <el-col :md="24" :offset="0">
         <h2>联系我们</h2>
         <el-row>
           <el-col :md="8" :offset="4">
             <div class="box1">
               <ul>
                 <li>Phone</li>
                 <li>17857242620</li>
                 <li>Email</li>
                 <li>1097546295@qq.com</li>
                 <li>Location</li>
                 <li>北下关街道上园村3号16号楼</li>
               </ul>
             </div>
           </el-col>
           <el-col :md="8" :offset="4">
             <div class="box2">
<!--               <img src="../assets/images/QRcode.jpg" alt="">-->
             </div>
           </el-col>
         </el-row>
       </el-col>
     </el-row>
   </header>
 </div>
</template>

<script>
export default {
  name: ''
}
</script>

<style lang="less" scoped>
  header {
    overflow: hidden;
    background: url(../../../assets/images/bkg2.jpg) no-repeat center;
    background-size: cover;
    height: 550px;
    h2 {
      text-align: center;
      color: #fff;
      font-size: 45px;
      margin: 40px;
    }
  }
  .box1 {
    margin-top: 50px;
    li:nth-of-type(odd){
      font-weight: bold;
      font-size: 25px;
      color: #fff;
      margin-bottom: 8px;
    }
    li:nth-of-type(even){
      font-size: 20px;
      color: #F8F9FA;
      margin-bottom: 20px;
    }
  }
  .box2 {
    margin-top: 30px;
    background: url(../../../assets/images/QRcode.jpg) no-repeat center;
    z-index: 10;
    height: 300px;
  }
</style>
