const content = document.querySelector('[data-tag="post-content"]');
const players = Array.from(content.querySelectorAll('p')).filter(e => !!e.querySelector('strong')).filter(e => !e.innerText.includes("Tier "));
const playerDetails = {}
players.forEach(e => {
    const rank = parseInt(e.querySelector('strong').innerText.split(')')[0])
    const name = e.querySelector('a > strong')?.innerText.trim();
    const details = e.querySelector('em')?.innerText.trim().split(" –")[0]
    playerDetails[name] = {details, rank}
})