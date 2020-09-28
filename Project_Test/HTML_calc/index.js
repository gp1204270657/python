function init1() {
    var num = document.getElementById("num")
    num.value = 0
    num.disabled = "disabled"

    var btnlist = document.getElementsByTagName("input")
    var btn_num1;
    var fh;
    for (var i = 0; i < btnlist.length; i++) {
        btnlist[i].onclick = function () {
            if (!isNaN(this.value)) {
                // num.value=(num.value+this.value)*1
                if (isNull(num.value)) {
                    num.value = this.value
                } else {
                    num.value = num.value + this.value
                }
            } else {
                var btn_num = this.value
                switch (btn_num) {
                    case  "+":
                        btn_num1 = Number(num.value)
                        fh = "+"
                        num.value = 0
                        break;
                    case "-":
                        btn_num1 = Number(num.value)
                        fh = "-"
                        num.value = 0
                        break;
                    case "*":
                        btn_num1 = Number(num.value)
                        fh = "*"
                        num.value = 0
                        break;
                    case "/":
                        btn_num1 = Number(num.value)
                        fh = "/"
                        num.value = 0
                        break;
                    case "=":
                        switch (fh) {
                            case "+":
                                num.value = btn_num1 + Number(num.value)
                                break;
                            case "-":
                                num.value = btn_num1 - Number(num.value)
                                break;

                            case "*":
                                num.value = btn_num1 * Number(num.value)
                                break;

                            case "/":
                                if (Number(num.value) == 0) {
                                    alert("除数不能为0")
                                    num.value = 0
                                } else {
                                    num.value = btn_num1 / Number(num.value)
                                    break;

                                }


                        }


                        break;
                    case "<—":
                        num.value = back(num.value)
                        break;
                    case ".":
                        num.value = xsd(num.value)


                        break;
                    case "B":

                        break;
                    case "+/-":
                        num.value = zfh(num.value)

                        break;
                    case "c":
                        num.value = "0"

                        break;
                }
            }

        }
    }
}


function zfh(n) {
    if (n.indexOf("-") == -1) {
        n = "-" + n
    } else {
        n = n.substr(1, n.length)
    }
    return n

}

function get1(n) {
    n = 0
}

/*退位键*/
function back(n) {
    n = n.substr(0, n.length - 1)
    if (isNull(n)) {
        n = 0
    }
    return n
}


/*
* 小数点*/
function xsd(n) {
    if (n.indexOf(".") == -1) {
        n = n + "."
    }
    return n

}

/*
判断里面数字时候为空
* */
function isNull(n) {
    if (n == 0 || n.length == 0) {
        return true
    } else {
        return false
    }
}


function bd() {
    document.getElementById("BD").onclick = function () {
        window.location.href="https://www.baidu.com"
    }
}