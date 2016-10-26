/**
 * 声明 & 定义
 */
var val; // 仅仅声明变量,此时的变量值是undefined
val = "hello"; // 变量赋值
var val2 = "world";//声明变量并且赋值.

/**
 * 简略声明变量
 */
val3 = "hello i am val3"; // 此时定义全局对象3，初始值是"hello i am val3"

/**
 * 作用范围
 */
function demo2(){
    var innerVal = "i am innerVal";
    console.log(innerVal); // 此时输出 "i am innerVal"
}
console.log(innerVal); // 此时输出undefined

/**
 * 不再区域(函数，对象)内声明的变量，为全局变量。此时作用域为全局
 */
function demo3(){
    demo3InnerVal = "definde in demo3,But regin is global";
    console.log(demo3InnerVal); //输出变量demo3InnerVal的内容
}
console.log(demo3InnerVal);//输出变量demo3InnerVal的内容