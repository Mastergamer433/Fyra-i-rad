const isValidMove = (col, board) => {
    for(let i = 0; i < board.length; i++){
        if (board[i][col] == 0){
            return true;
        }
    }
    return false;
};

const getRowBasedOnCol = (col, board) =>{
    for(let i=0;i<board.length;i++){
        if(board[i][col] == 0){
            return i;
        }
    }
    return null;
};


       
const checkForWin = (board_array, chip) => {
    for(let i = 0; i < board_array.length; i++){
        for(let j = 0; j < board_array[i].length - 3; j++){
            if(
                board_array[i][j] == chip &&
                board_array[i][j+1] == chip &&
                board_array[i][j+2] == chip &&
                board_array[i][j+3] == chip){
                
                return true;
            }
        }
    }
    
    for(let i = 0; i < board_array.length - 3; i++){
        for(let j = 0; j < board_array[i].length; j++){
            if(
                board_array[i][j] == chip &&
                board_array[i+1][j] == chip &&
                board_array[i+2][j] == chip &&
                board_array[i+3][j] == chip){
                return true;
            }
        }
    }
    
    for(let i = board_array.length - 3; i < board_array.length; i++){
        for(let j = board_array[i].length - 3; j < board_array[i].length; j++){
            if(
                board_array[i][j] == chip &&
                board_array[i-1][j-1] == chip &&
                board_array[i-2][j-2] == chip &&
                board_array[i-3][j-3] == chip
            ){
                return true
            }
        }
    }

    for(let i = 0; i < 3; i++){
        for(let j = 0; j < 3; j++){
            if(
                board_array[i][j] == chip &&
                board_array[i+1][j+1] == chip &&
                board_array[i+2][j+2] == chip &&
                board_array[i+3][j+3] == chip 
            ){
                return true;
            }
        }
    }
    return false;
};

module.exports.isValidMove = isValidMove;
module.exports.getRowBasedOnCol = getRowBasedOnCol;
module.exports.checkForWin = checkForWin;
