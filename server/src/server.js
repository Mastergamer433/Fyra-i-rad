const logic = require('./logic.js');
const array = require('./array.js');
let sockets = [];
sockets.broadcast = async (msg) => {
    for(let socket in sockets){
        socket.write(msg);
    }
};
let turn = 1;
let board = []; 
let rows = 6;
let columns = 7;
const socketHandler = async(socket) => {
    sockets.push(socket);
    board = array.createBoard();
    console.log(board);
    socket.mark = sockets.length;
    socket.on('data', (data) => {
        socket.setEncoding('utf8');
        const dataSplit = data.toString().split('\n\n');
        const type = dataSplit[0];
        const message = dataSplit[1];
        console.log(message, type);
        if (type == 'Socket') {
            if (message == 'DISCONNECT') {
                socket.write('OK');
                socket.end();
                delete sockets[socket];
            }
        }
        else if(type == 'Board'){
            if(message == 'Get'){
                console.log(JSON.stringify(board).split('').length);
                socket.write(`${JSON.stringify(board).split('').length}\n`);
                socket.write(JSON.stringify(board));
            }
        }
        else if(type == 'Move'){
            console.log(socket.mark, turn);
            if(socket.mark == turn){
                if (logic.isValidMove(message, board)){
                    let row = logic.getRowBasedOnCol(message, board);
                    if(row != null){
                        board[row][message] = turn;
                        console.log(board)
                        socket.write(`${JSON.stringify(board).split('').length}\n`);
                        socket.write(JSON.stringify(board));
                        if(logic.checkForWin(board, turn, rows, columns)){
                            let message = `${turn}`;
                            sockets.broadcast(message.split('').length);
                            sockets.broadcast(message);
                        }else{
                            console.log('no winner');
                            socket.write('1');
                            socket.write('0');
                            console.log('no winner');
                        }
                        turn == 1 ? turn = 2 : turn = 1;
                        console.log(message);
                    }
                }else{
                    socket.write('1');
                    socket.write('0');
                }
                
        
            }else{
                socket.write('1');
                socket.write('0');
            }
        }
        else if(type == 'What is?'){
            if(message == 'Player'){
                socket.write('1');
                socket.write(socket.mark.toString());
                console.log(socket.mark.toString());
            }
        }
    });
};
const net = require('net');
const server = net.createServer(socketHandler);
server.listen(5673);
