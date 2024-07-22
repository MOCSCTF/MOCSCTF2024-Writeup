<?php 
highlight_file(__FILE__);
//Php 1s Never Die!!!
ini_set('open_basedir','/var/www/html/');
function filter($str){
    if(preg_match('/passthru|\`|exec|call_user_func|pcntl|shell|popen|ob_start|map|array|system/i', $str)){
        return 'Damn Hacker🙉!';
    }
    else{
        return $str;
    }
}
filter(eval($_POST['1']));
?>