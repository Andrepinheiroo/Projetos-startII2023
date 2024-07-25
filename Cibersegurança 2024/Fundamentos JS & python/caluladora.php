CalculadoraPHP.txt
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora PHP</title>
</head>
<body>
    <h2>Calculadora</h2>
    <form action="" method="POST">
        <input type="number" name="num1" required="" placeholder="Número 1">
        <input type="number" name="num2" required="" placeholder="Número 2">
        <select name="operation" required="">
            <option value="add">+</option>
            <option value="sub">-</option>
            <option value="mult">*</option>
            <option value="div">/</option>
        </select>
        <input type="submit" name="" value="Calcular">
    </form>
    <?php
    if ($_POST) {
        $num1 = $_POST['num1'];
        $num2 = $_POST['num2'];
        $operation = $_POST['operation'];

        switch ($operation) {
            case "add":
                $result = $num1 + $num2;
                break;
            case "sub":
                $result = $num1 - $num2;
                break;
            case "mult":
                $result = $num1 * $num2;
                break;
            case "div":
                if ($num2 != 0) {
                    $result = $num1 / $num2;
                } else {
                    $result = "Impossível Dividir por ZERO!";
                }
                break;
            default:
                $result = "Operação inválida";
                break;
        }
        echo "Resultado: " . $result;
    }
    ?>
</body>
</html>