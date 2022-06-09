const createBoard = () => {
    let board = [];
    for(let i = 0; i < 6; i++){
        board.push([]);
        for(let j = 0; j < 7; j++){
            board[i].push(0);
        }
    }
    board[3][1] = 1;
    board[2][3] = 2;
    return board;
};

module.exports.createBoard = createBoard;
