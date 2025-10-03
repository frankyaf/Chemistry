import '../App.css';

export function Board(){
    const rows = 10;
    const cols = 18;
    const cuadros = Array.from({ length: rows * cols });
    return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="grid gap-1 bg-gray-300 p-1" 
        style={{
            gridTemplateRows: `repeat(${rows}, 30px)`,
            gridTemplateColumns: `repeat(${cols}, 30px)`,
            }}
      >
        {cuadros.map((_, index) => (
          <div
            key={index}
            className="w-20 h-20 bg-blue-500 border border-gray-200"
          />
        ))}
      </div>
    </div>
    )
}