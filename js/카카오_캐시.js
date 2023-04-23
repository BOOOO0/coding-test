function solution(cacheSize, cities) {
  var answer = 0;
  // 일단은 그냥 큐로 메모리를 구현을 했는데
  // LRU를 사용한다고 하니까
  // head와 tail을 구분해서 해줘야 할 것 같은데
  // 근데 그냥 LRU만 되나 LRU 근사는 안되나
  // 어차피 LRU도 완전한 LRU는 안될거다

  // 캐시크기 0일때 바로 return 해주는거 넣어주니까 됐는데
  // 옆에 예제는 통과인데 왜...
  if (!cacheSize) return cities.length * 5;
  let cache = new Array(cacheSize);
  cities = cities.map((e) => e.toLowerCase());
  for (let x of cities) {
    if (!cache.includes(x)) {
      if (cache.length !== cacheSize) cache.push(x);
      else {
        cache.shift();
        cache.push(x);
      }
      answer += 5;
    } else {
      // 캐시가 꽉찬 상태에서의 cache hit라면
      // 캐시 안에 있는 해당 도시를 splice 시키고 최신이 tail 이니까
      // 새로 push 해준다.
      // 테케 2개 안되네 짜증~ ^^

      // 1 2 3  2가참조되었다
      // 1 3 2
      let idx = cache.indexOf(x);
      cache.splice(idx, 1);
      cache.push(x);
      // 아 cache가 꽉차기 전에도 cache hit는 일어날 수 있다
      // 그래도 2개 안돼~ ^^
      answer += 1;
    }
  }
  // LRU 언제 참조되었는지를 어떻게 표현할지를
  // 큐의 head 참조된지 오래된거 tail 최신 참조
  return answer;
}
