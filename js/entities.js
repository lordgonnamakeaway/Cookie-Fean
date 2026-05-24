// Game Entities

class Player {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.width = PLAYER_WIDTH;
        this.height = PLAYER_HEIGHT;
        this.velocityX = 0;
        this.speed = PLAYER_SPEED;
    }

    moveLeft() {
        this.velocityX = -this.speed;
    }

    moveRight() {
        this.velocityX = this.speed;
    }

    update() {
        this.x += this.velocityX;

        // Boundary checking
        if (this.x - this.width / 2 < 0) {
            this.x = this.width / 2;
        } else if (this.x + this.width / 2 > SCREEN_WIDTH) {
            this.x = SCREEN_WIDTH - this.width / 2;
        }

        // Friction
        this.velocityX *= 0.9;
    }

    draw(ctx) {
        // Draw player body (rectangle)
        ctx.fillStyle = COLORS.PLAYER;
        ctx.fillRect(
            this.x - this.width / 2,
            this.y - this.height / 2,
            this.width,
            this.height
        );

        // Draw rounded corners effect
        ctx.strokeStyle = COLORS.DARK_BLUE;
        ctx.lineWidth = 3;
        ctx.strokeRect(
            this.x - this.width / 2,
            this.y - this.height / 2,
            this.width,
            this.height
        );

        // Draw player head (circle)
        const headCenterX = this.x;
        const headCenterY = this.y - this.height / 3;
        const headRadius = this.width / 6;

        ctx.fillStyle = COLORS.SKIN;
        ctx.beginPath();
        ctx.arc(headCenterX, headCenterY, headRadius, 0, Math.PI * 2);
        ctx.fill();

        // Draw eyes
        const eyeOffset = this.width / 10;
        const eyeY = headCenterY - this.width / 15;
        
        ctx.fillStyle = COLORS.BLACK;
        ctx.beginPath();
        ctx.arc(headCenterX - eyeOffset, eyeY, 4, 0, Math.PI * 2);
        ctx.fill();

        ctx.beginPath();
        ctx.arc(headCenterX + eyeOffset, eyeY, 4, 0, Math.PI * 2);
        ctx.fill();

        // Draw smile
        ctx.strokeStyle = COLORS.BLACK;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(headCenterX, headCenterY + 5, 8, 0, Math.PI);
        ctx.stroke();

        // Draw basket (catching area)
        ctx.fillStyle = COLORS.BASKET;
        ctx.fillRect(
            this.x - this.width / 3,
            this.y + this.height / 4,
            this.width / 1.5,
            this.height / 3
        );

        ctx.strokeStyle = COLORS.DARK_BLUE;
        ctx.lineWidth = 2;
        ctx.strokeRect(
            this.x - this.width / 3,
            this.y + this.height / 4,
            this.width / 1.5,
            this.height / 3
        );
    }

    getCollisionRect() {
        return {
            x: this.x - this.width / 2,
            y: this.y - this.height / 2,
            width: this.width,
            height: this.height
        };
    }
}

class Cookie {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.velocityY = COOKIE_FALL_SPEED;
        this.size = COOKIE_SIZE;
        this.rotation = 0;
        this.rotationSpeed = 5;
    }

    update() {
        this.y += this.velocityY;
        this.velocityY += GRAVITY;

        // Cap maximum velocity
        if (this.velocityY > MAX_COOKIE_VELOCITY) {
            this.velocityY = MAX_COOKIE_VELOCITY;
        }

        this.rotation += this.rotationSpeed;
    }

    draw(ctx) {
        // Draw cookie circle
        ctx.fillStyle = COLORS.COOKIE;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size / 2, 0, Math.PI * 2);
        ctx.fill();

        // Draw border
        ctx.strokeStyle = COLORS.CHIP;
        ctx.lineWidth = 2;
        ctx.stroke();

        // Draw chocolate chips
        const chipCount = 8;
        ctx.fillStyle = COLORS.CHIP;

        for (let i = 0; i < chipCount; i++) {
            const angle = (360 / chipCount) * i + (this.rotation % 360);
            const rad = (angle * Math.PI) / 180;
            const chipX = this.x + Math.cos(rad) * (this.size / 3);
            const chipY = this.y + Math.sin(rad) * (this.size / 3);

            ctx.beginPath();
            ctx.arc(chipX, chipY, 3, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    getCollisionRect() {
        return {
            x: this.x - this.size / 2,
            y: this.y - this.size / 2,
            width: this.size,
            height: this.size
        };
    }
}

class Chute {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.width = CHUTE_WIDTH;
        this.height = CHUTE_HEIGHT;
    }

    draw(ctx) {
        // Draw chute body
        ctx.fillStyle = COLORS.CHUTE;
        ctx.fillRect(
            this.x - this.width / 2,
            this.y,
            this.width,
            this.height
        );

        // Draw chute border
        ctx.strokeStyle = COLORS.BLACK;
        ctx.lineWidth = 2;
        ctx.strokeRect(
            this.x - this.width / 2,
            this.y,
            this.width,
            this.height
        );

        // Draw chute opening (darker)
        ctx.fillStyle = COLORS.CHUTE_OPENING;
        ctx.fillRect(
            this.x - this.width / 3,
            this.y + this.height - 10,
            this.width / 1.5,
            10
        );

        // Draw opening border
        ctx.strokeStyle = COLORS.BLACK;
        ctx.lineWidth = 1;
        ctx.strokeRect(
            this.x - this.width / 3,
            this.y + this.height - 10,
            this.width / 1.5,
            10
        );
    }
}

class Particle {
    constructor(x, y, vx, vy, lifetime = 30, color = '#ffd700') {
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
        this.lifetime = lifetime;
        this.maxLifetime = lifetime;
        this.color = color;
        this.size = 5;
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;
        this.vy += GRAVITY;
        this.lifetime--;
    }

    draw(ctx) {
        const alpha = this.lifetime / this.maxLifetime;
        ctx.globalAlpha = alpha;

        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();

        ctx.globalAlpha = 1.0;
    }

    isAlive() {
        return this.lifetime > 0;
    }
}

// Collision detection utility
function checkCollision(rect1, rect2) {
    return (
        rect1.x < rect2.x + rect2.width &&
        rect1.x + rect1.width > rect2.x &&
        rect1.y < rect2.y + rect2.height &&
        rect1.y + rect1.height > rect2.y
    );
}
