registrar.php
<?php
require_once("bootstrap.php");
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Registrar PHP</title>
</head>
<body>
    <h2>Registrar</h2>
    <form action="" method="post">
        Nome Completo:
        <input name="nome" type="text" placeholder="Ex: Felipe Melo" required><br>
        E-mail:
        <input name="email" type="email" placeholder="E-mail" required><br>
        Senha:
        <input name="senha1" type="password" placeholder="6 ou mais dígitos" autocomplete="off" required><br>
        Repita a Senha:
        <input name="senha2" type="password" placeholder="Confirme sua senha" autocomplete="off" required><br>

        <input type="checkbox" require="" name="termos">Li e aceito os Termos e Condições<br>

        <button type="submit" class="btn btn-block mt-lg btn-default"><b>Cadastrar</b></button>
    </form>
    
</body>
</html>

<?php

if($_POST){
    date_default_timezone_set('Brazil/East');

    $nome = $_POST['nome'];
    $nome = htmlspecialchars($nome, ENT_QUOTES);

    $email = $_POST['email'];
    $email = htmlspecialchars($email, ENT_QUOTES);

    $termos = $_POST['termos'];
    $termos = htmlspecialchars($termos, ENT_QUOTES);

    $senha1 = $_POST['senha1'];
    $senha1 = htmlspecialchars($senha1, ENT_QUOTES);

    $senha2 = $_POST['senha2'];
    $senha2 = htmlspecialchars($senha2, ENT_QUOTES);

    $senhacript = hash('sha256', $senha1);

    $data = date("Y-m-d H:i:s");

    $ip = $_SERVER['REMOTE_ADDR'];

    if(empty($email)){
        echo "<script>window.alert('Digite seu e-mail!');</script>";
        echo "<meta http-equiv='refresh' content='0;'>";
        return false;
    }
    
    $veric = mysqli_query($conn, "SELECT * FROM users WHERE email='$email'");
    $verifc = mysqli_num_rows($veric);

    if($verifc == true) {
        echo "<script>window.alert('Você já está cadastrado!');</script>";
        echo "<meta http-equiv='refresh' content='0;'>";
        return false;
    }
    
    if(empty($termos)){
        echo "<script>window.alert('Concorde com os Termos!');</script>";
        echo "<meta http-equiv='refresh' content='0;'>";
        return false;
    }

    if(empty($senha1)){
        echo "<script>window.alert('Digite uma senha!');window.history.go(-1);</script>";
        return false;
    }

    if(empty($senha2)){
        echo "<script>window.alert('Confirme sua senha!');window.history.go(-1);</script>";
        return false;
    }

    if($senha1 != $senha2){
        echo "<script>window.alert('Senhas Diferentes!');</script>";
        echo "<meta http-equiv='refresh' content='0;'>";
        return false;
    }

    /////// Granvando no Banco ///////
    $sql1 = mysqli_query($conn, "INSERT INTO users(nome, email, senha, data, ip) VALUES ('$nome','$email', '$senhacript', '$data', '$ip')");
}

?>