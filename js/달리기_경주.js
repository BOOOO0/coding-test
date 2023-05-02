let players = ["mumu", "soe", "poe", "kai", "mine"];
let callings = ["kai", "kai", "mine", "mine"];

function solution(players, callings) {
  const idxs = {};

  for (let i = 0; i < players.length; i++) {
    idxs[players[i]] = i;
  }

  callings.forEach((player) => {
    const curIdx = idxs[player];

    const nextplayer = players[curIdx - 1];

    players[curIdx - 1] = player;
    players[curIdx] = nextplayer;

    idxs[player]--;
    idxs[players[curIdx]]++;
  });

  return players;
}

solution(players, callings);

// function solution(players, callings) {
//   var answer = [];

//   let playerMap = {};
//   for (let i = 0; i < players.length; i++) {
//     playerMap[players[i]] = i + 1;
//   }

//   while (callings.length > 0) {
//     let called = callings.shift();
//     let keys = Object.keys(playerMap);

//     let frontRank = playerMap[called] - 1;
//     let front = keys.find((key) => {
//       if (playerMap[key] === frontRank) {
//         return key;
//       }
//     });

//     playerMap[called] -= 1;
//     playerMap[front] += 1;
//   }
//   let result = Object.fromEntries(
//     Object.entries(playerMap).sort(([, a], [, b]) => (a < b ? -1 : 1))
//   );
//   answer = Object.keys(result);
//   return answer;
// }

// function solution(players, callings) {
//   let nameMap = new Map();
//   let rankMap = new Map();

//   players.forEach((e, i) => {
//     nameMap.set(e, i);
//     rankMap.set(i, e);
//   });

//   while (callings.length > 0) {
//     let called = callings.shift();
//     let calledRank = nameMap.get(called);
//     let front = rankMap.get(calledRank - 1);
//     let frontRank = nameMap.get(front);

//     nameMap.set(called, calledRank - 1);
//     rankMap.set(calledRank, front);
//     nameMap.set(front, calledRank);
//     rankMap.set(calledRank - 1, called);
//   }

//   let result = new Map([...nameMap].sort(([, a], [, b]) => (a < b ? -1 : 1)));

//   let answer = result.keys();

//   return answer;
// }
