<body>
    <h2>Login</h2>
    <form action="" method="POST">
        <input type="text" name="user" required="" placeholder="Usuário">
        <input type="password" name="pass" required="" placeholder="Senha">
        <input type="submit" name="" value="Entrar">
    </form>
    <?php
    if ($_POST){
        $user = $_POST['user'];
        $pass = $_POST['pass'];
        
        if ($user == "felipe" && $pass == "123456"){
            echo "Acesso permitido";
        }else {
            echo "Acesso negado";
        }
    }
    ?>

</body>

